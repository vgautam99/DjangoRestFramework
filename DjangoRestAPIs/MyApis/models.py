from datetime import datetime
from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=datetime.utcnow())
