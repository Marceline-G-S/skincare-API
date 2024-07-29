from rest_framework import serializers
from skincareapi.models import Customer
from skincareapi.serializers import SkintypeSerializer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    skintype = SkintypeSerializer(read_only=True)  # Assuming SkintypeSerializer exists
    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(view_name='customer', lookup_field='id')
        fields = ('id', 'skintype')
        depth = 1