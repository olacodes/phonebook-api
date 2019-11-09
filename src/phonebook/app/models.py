from django.db import models

# Create your models here.
class Phonebook(models.Model):
    lastname = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=25, default="000000000")
    email = models.EmailField(max_length=254, unique=True)
    address = models.TextField(max_length=255)

    def __str__(self):
        return self.lastname

