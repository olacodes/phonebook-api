from django.urls import path, include
from phonebook.app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.PhonebookView)

urlpatterns = [
    path('', include(router.urls))
]
