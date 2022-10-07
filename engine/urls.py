from django.urls import path
from .views import my_name


urlpatterns = [
    path('car/', my_name),
]
