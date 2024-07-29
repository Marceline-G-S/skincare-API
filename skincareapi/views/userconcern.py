from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from skincareapi.models import UserConcern, Customer, Concern
from skincareapi.serializers import UserConcernSerializer
from django.contrib.auth.models import User

class UserConcernsViewSet(ViewSet):
    
    def list(self, request):
        try:
            userConcerns = UserConcern.objects.filter(user=request.auth.user)
            serializer = UserConcernSerializer(userConcerns, many=True, context={"request": request})
            return Response(serializer.data)
        except UserConcern.DoesNotExist as ex:
            return Response(
                {
                    "message": "The requested UserConcern does not exist, or you do not have permission to access it."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        current_user = Customer.objects.get(user=request.auth.user)

        try:
            concern = request.data["concern"]
            UserConcern.objects.get(user=current_user.user, concern=concern)
        except UserConcern.DoesNotExist as ex:
            new_user_concern = UserConcern()
            new_user_concern.user = current_user.user
            new_user_concern.concern = Concern.objects.get(id=concern)
            new_user_concern.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """
        @api {DELETE} /userconcerns/
        In body : concern: [id of concern]
        HTTP/1.1 204 No Content
        """
        try:
            current_user = Customer.objects.get(user=request.auth.user)
            concern = request.data["concern"]
            user_concern = UserConcern.objects.get(user=current_user, concern=concern)
            user_concern.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
                        return Response(
                {
                    "message": "The requested UserConcern does not exist, or you do not have permission to access it."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        