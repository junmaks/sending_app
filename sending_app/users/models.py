import uuid

from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    phone_number = models.CharField(max_length=11)
    code_mobile_operator = models.CharField(max_length=30)
    tag = models.CharField(max_length=255, default=None)
    time_zone = models.CharField(max_length=255, default=None)
