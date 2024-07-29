# serializers/skintype_serializer.py
from rest_framework import serializers
from skincareapi.models import Skintype

class SkintypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skintype
        fields = ['id','skintype']
