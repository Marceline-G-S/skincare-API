# serializers/skintype_serializer.py
from rest_framework import serializers
from skincareapi.models import Concern

class ConcernSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concern
        fields = ['id','concern']
