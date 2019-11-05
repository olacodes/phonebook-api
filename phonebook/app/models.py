from django.db import models

# Create your models here.
class Phonebook(models.Model):

    lastname=models.CharField(max_length=255)
    firstname=models.CharField(max_length=255)
    phoneno=models.CharField(max_length=20)
    email=models.CharField(max_length=255)
    address=models.TextField(max_length=255)


