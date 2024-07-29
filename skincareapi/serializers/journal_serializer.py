from rest_framework import serializers
from skincareapi.models import Journal
from .concern_serializer import ConcernSerializer

class JournalSerializer(serializers.ModelSerializer):
    concern = ConcernSerializer(read_only=True)

    class Meta:
        model = Journal
        fields = ['id', 'user', 'concern', 'description', 'date']