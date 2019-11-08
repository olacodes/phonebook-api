from .models import Phonebook
from .serializers import PhonebookSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PhonebookList(APIView):
    """
    List all phonebooks, or create a new phonebook
    """

    def get(self, request):
        phonebooks = Phonebook.objects.all()
        serializer = PhonebookSerializer(phonebooks, many=True)
        return Response(serializer.data)

    def post(self, request):

        phonebook = PhonebookSerializer(data=request.data)
        if phonebook.is_valid():
            phonebook.save()
            return Response(phonebook.data, status=status.HTTP_201_CREATED)
        return Response(phonebook.errors, status=status.HTTP_400_BAD_REQUEST)

class PhonebookDetail(APIView):
    """
    Retrieve, update or delete a phonebook instance
    """

    def get_phonebook(self, pk):
        try:
            return Phonebook.objects.get(pk=pk)
        except Phonebook.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        phonebook = self.get_phonebook(pk)
        serializer = PhonebookSerializer(phonebook)
        return Response(serializer.data)

    def put(self, request, pk):
        phonebook = self.get_phonebook(pk)
        serializer = PhonebookSerializer(phonebook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        phonebook = self.get_phonebook(pk)
        phonebook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Phonebook
# from .serializers import PhonebookSerializer

# class PhonebookView(viewsets.ModelViewSet):
#     queryset = Phonebook.objects.all()
#     serializer_class = PhonebookSerializer
