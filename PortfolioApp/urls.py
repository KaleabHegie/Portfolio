from django.urls import path
from django.conf import settings

from .views import (
   onepage
) 

urlpatterns = [
     path('', onepage, name='onepage'),
]
