from django.db import models
from django.contrib.auth.models import User
from .concerns import Concern


class Journal(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='concern')
    concern = models.ForeignKey(Concern, on_delete=models.DO_NOTHING, related_name='user')
    description = models.CharField(max_length=500)
    date = models.DateField(default="0000-00-00")