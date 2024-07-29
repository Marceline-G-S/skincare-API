from django.db import models


class Skintype(models.Model):

    skintype = models.CharField(max_length=15)