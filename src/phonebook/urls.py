from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('phonebook.app.urls'), name="api"),
    path('admin/', admin.site.urls)
    # path('admin/', admin.site.urls)

]
