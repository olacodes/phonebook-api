from django.urls import path, include
from phonebook.app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("phonebook/", views.PhonebookList.as_view()),
    path("phonebook/<int:pk>/", views.PhonebookDetail.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)