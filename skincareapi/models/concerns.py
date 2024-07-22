from django.db import models


class Concern(models.Model):

    concern = models.CharField(max_length=25)
    description = models.CharField(max_length=100)