from rest_framework import serializers
from .models import Phonebook

class PhonebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonebook
        fields = ["id", "lastname", "firstname", "phone_number", "email", "address"]