from django.db import models
from django.contrib.auth.models import User
from .concerns import Concern


class UserConcern(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='concern')
    concern = models.ForeignKey(Concern, on_delete=models.DO_NOTHING, related_name='user')