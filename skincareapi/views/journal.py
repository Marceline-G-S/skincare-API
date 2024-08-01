from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from skincareapi.models import Customer, Journal, Concern
from skincareapi.serializers import JournalSerializer
from django.contrib.auth.models import User
import datetime

class JournalViewSet(ViewSet):

    def retrieve(self, request, pk=None):
        """
        @api {GET} /journal/[journal id]
        HTTP/1.1 200 
        Content : return journal entry if belongs to user
        """
        try:
            userJournal = Journal.objects.get(user=request.auth.user, pk=pk)
            serializer = JournalSerializer(userJournal, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """
        @api {GET} /journal
        HTTP/1.1 200 
        Content : List of journal's with user
        """
        try:
            userJournals = Journal.objects.filter(user=request.auth.user)
            serializer = JournalSerializer(userJournals, many=True, context={"request": request})
            return Response(serializer.data)
        except Journal.DoesNotExist as ex:
            return Response(
                {
                    "message": "The requested Journal does not exist, or you do not have permission to access it."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """
        @api {POST} /journal
        In body : description : "description of journal entry",
        concern : [concern id here]
        HTTP/1.1 204 No Content
        """
        new_journal = Journal()
        customer_user = Customer.objects.get(user=request.auth.user)
        new_journal.user = customer_user.user
        new_journal.concern = Concern.objects.get(id=request.data["concern"])
        new_journal.description = request.data["description"]
        new_journal.date = datetime.datetime.now()
        new_journal.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        """
        @api {PUT} /journal/[anynumber]
        In body : id: [id journal],
        description : "description here",
        concern : [id of concern here]
        HTTP/1.1 204 No Content
        """
        # fetch customer matching user making req
        customer = Customer.objects.get(user=request.auth.user)
        # fetch journal id from request body
        journal_id = request.data["id"]
        # fetch Journal with provided pk
        journal_to_edit = Journal.objects.get(pk=journal_id, user=customer.user)
        # extract and assign description and concern
        journal_to_edit.description = request.data["description"]
        journal_to_edit.concern = Concern.objects.get(id=request.data["concern"])
        journal_to_edit.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """
        @api {DELETE} /journal/[journal id here]
        HTTP/1.1 204 No Content
        """
        try:
            current_user = Customer.objects.get(user=request.auth.user)
            user_concern = Journal.objects.get(user=current_user.user, id=pk)
            user_concern.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
                        return Response(
                {
                    "message": "The requested journal does not exist, or you do not have permission to access it."
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        