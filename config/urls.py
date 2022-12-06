from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('kommandant/', admin.site.urls),
]
