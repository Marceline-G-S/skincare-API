from django.db import models
from django.contrib.auth.models import User
from .skintypes import Skintype


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
    skintype = models.ForeignKey(Skintype, on_delete=models.DO_NOTHING, related_name='users')