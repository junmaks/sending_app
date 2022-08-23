from rest_framework.response import Response
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import ClientSerializer
from .models import Client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer