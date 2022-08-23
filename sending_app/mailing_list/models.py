import datetime
import uuid
from django.db import models

# Create your models here.
class Mailing(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    date_start = models.DateTimeField()
    text_message = models.CharField(max_length=500)
    filter_mailing = models.CharField(max_length=255, default=None)
    date_end = models.DateTimeField()


class Message(models.Model):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    date_start = models.DateTimeField(auto_now_add=True)
    status_sending = models.CharField(max_length=255, )
    mailing_id = models.ForeignKey('Mailing', on_delete=models.CASCADE, null=False, default=None)
    client_id = models.ForeignKey('users.client', on_delete=models.CASCADE, null=False, default=None)
