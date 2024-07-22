from django.db import models
from django.contrib.auth.models import User


class Skintype(models.Model):

    skintype = models.CharField(max_length=15)