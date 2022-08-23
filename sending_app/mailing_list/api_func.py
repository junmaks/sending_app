import requests

from .models import Message, Mailing
from users.models import Client
from rest_framework.response import Response
from .mailing_enums import *
from django.db.models import Q
from .serializer import MessageSerializer


def get_mailing_statistic(pk):
    try:
        instance = Mailing.objects.get(pk=pk)
        success_count = Message.objects.filter(mailing_id=instance.id, status_sending=SENT_message).count()
        pending_count = Message.objects.filter(mailing_id=instance.id, status_sending=PENDING_message).count()
        fail_count = Message.objects.filter(mailing_id=instance.id, status_sending=FAIL_message).count()
        response_object = {
            'id': str(instance.id),
            'date_start': instance.date_start,
            'text_message': instance.text_message,
            'filter_mailing': instance.filter_mailing,
            'date_end': instance.date_end,
            'messages_count': {
                'success': success_count,
                'pending': pending_count,
                'fail': fail_count,
            },
            'messages': [],
        }
        messages = Message.objects.filter(mailing_id=pk).all()
        if len(messages):
            for message in messages:
                response_object['messages'].append({
                    'id': str(message.id),
                    'date_start': message.date_start,
                    'status_sending': message.status_sending,
                    'client_id': str(message.client_id_id),
                    'mailing_id': str(message.mailing_id_id),
                })

        return Response({'mailing_statistic': response_object})
    except Exception as ex:
        return Response({'error': str(ex)})


def get_all_statistic():
    response_object = []
    mailing_list = Mailing.objects.all()
    for mailing in mailing_list:
        success_count = Message.objects.filter(mailing_id=mailing.id, status_sending=SENT_message).count()
        pending_count = Message.objects.filter(mailing_id=mailing.id, status_sending=PENDING_message).count()

        response_object.append({
            'mailing_id': str(mailing.id),
            'count_messages': {'success': success_count,
                               'pending': pending_count, }
        })
    return Response({'statistic': response_object})


def post_new_message(pk):
    try:
        sending_messages(pk).delay()
        return Response({'Message': 'Success'})
    except Exception as ex:
        return Response({'error': str(ex)})


