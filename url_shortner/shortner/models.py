from django.db import models
import uuid

class URL(models.Model):
    link = models.CharField(max_length = 1000)
    new = models.CharField(max_length = 6)
    uuid = models.UUIDField(primary_key = True, default=uuid.uuid4(), editable = True, max_length=36)
