from rest_framework import viewsets
from skincareapi.models import Skintype
from skincareapi.serializers import SkintypeSerializer

class SkintypeViewSet(viewsets.ModelViewSet):
    queryset = Skintype.objects.all()
    serializer_class = SkintypeSerializer
    http_method_names = ['get']  # Only allow GET requests