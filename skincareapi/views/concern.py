from rest_framework import viewsets
from skincareapi.models import Concern
from skincareapi.serializers import ConcernSerializer

class ConcernViewSet(viewsets.ModelViewSet):
    queryset = Concern.objects.all()
    serializer_class = ConcernSerializer
    http_method_names = ['get']  # Only allow GET requests