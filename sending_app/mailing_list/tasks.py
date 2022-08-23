import datetime
import pytz

import requests
from django.db.models import Q

from users.models import Client
from .mailing_enums import *
from .models import Mailing, Message
from sending_app.celery import app
from .api_func import post_new_message
from .serializer import MessageSerializer


@app.task
def check_mailing():
    mailing_list = Mailing.objects.all()
    for mailing in mailing_list:
        date_now = datetime.datetime.now(datetime.timezone.utc)
        if date_now >= mailing.date_start and date_now <= mailing.date_end:
            sending_messages.delay(mailing.pk)


@app.task
def sending_messages(pk):
    mailing_item = Mailing.objects.get(pk=pk)
    clients = Client.objects.filter \
        (Q(code_mobile_operator=mailing_item.filter_mailing) | Q(tag=mailing_item.filter_mailing))
    for client in clients:
        message = Message.objects.filter(Q(client_id=client.id) & Q(mailing_id=mailing_item.id))
        if message:
            continue
        else:
            message_data = {
                'status_sending': PENDING_message,
                'client_id': client.id,
                'mailing_id': mailing_item.id,
            }
            serializer = MessageSerializer(data=message_data)
            serializer.is_valid(raise_exception=True)
            new_message = Message.objects.create(
                status_sending=message_data['status_sending'],
                client_id_id=message_data['client_id'],
                mailing_id_id=message_data['mailing_id'],
            )

            header = {"Authorization": 'Bearer {}'.format(TOKEN_token),
                      'Content-Type': 'application/json'
                      }
            data = {
                "id": int(new_message.id),
                "phone": int(client.phone_number),
                "text": str(mailing_item.text_message),
            }

            response = requests.post(f'https://probe.fbrq.cloud/v1/send/{new_message.id}',
                                     headers=header,
                                     json=data,
                                     )

            if response.status_code == 200:
                status_message = SENT_message
            else:
                status_message = FAIL_message

            new_message.status_sending = status_message
            new_message.save()