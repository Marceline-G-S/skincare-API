from rest_framework import serializers
from skincareapi.models import UserConcern
from .concern_serializer import ConcernSerializer

class UserConcernSerializer(serializers.ModelSerializer):
    concern = ConcernSerializer(read_only=True)

    class Meta:
        model = UserConcern
        fields = ['id', 'user', 'concern']