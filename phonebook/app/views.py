from django.shortcuts import render
from rest_framework import viewsets
from .models import Phonebook
from .serializers import PhonebookSerializer

class PhonebookView(viewsets.ModelViewSet):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer

