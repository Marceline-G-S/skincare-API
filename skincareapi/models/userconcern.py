from django.db import models
from django.contrib.auth.models import User
from .concern import Concern


class UserConcern(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concern = models.ForeignKey(Concern, on_delete=models.CASCADE)