from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from skincareapi.models import Customer, Skintype
from skincareapi.serializers import CustomerSerializer

class CustomersViewSet(ViewSet):

    def update(self, request, pk=None):
        try:
            customer = Customer.objects.get(user=request.auth.user)
            # extract skinytpe ID from request data
            skintype_id = request.data["skintype"]
            username = request.data["username"]
            password = request.data["password"]

            skintype = Skintype.objects.get(pk=skintype_id)

            # assign fetched skin type to the customer's skin type field
            customer.skintype = skintype
            customer.user.username = username
            customer.user.password = password

            customer.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Customer.DoesNotExist as ex:
            return Response({"message": "Customer does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        try:
            customer = Customer.objects.get(user=request.auth.user)
            serializer = CustomerSerializer(customer, context={"request": request})
            return Response(serializer.data)
        except Customer.DoesNotExist as ex:
            return Response(
                {
                    "message": "The requested customer does not exist, or you do not have permission to access it."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as ex:
            return HttpResponseServerError(ex)
        

