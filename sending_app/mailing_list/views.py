

from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import MessageSerializer, MailingSerializer
from .models import Message, Mailing
from rest_framework.views import APIView
from .api_func import get_mailing_statistic, get_all_statistic, post_new_message


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class AllStatisticView(APIView):
    def get(self, request):
        return get_all_statistic()


class MailingStatisticView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            if not pk:
                return Response({'error': 'Method GET not allowed'})
            else:
                return get_mailing_statistic(pk)
        except Exception as ex:
            return Response({'error': str(ex)})
