from django.urls import path
from django.conf import settings

from .views import (
    index ,  projects , onepage
) 

urlpatterns = [
     path('', index, name='index'),
     path('projects/', projects, name='projects'),
     path('onepage/', onepage, name='onepage'),
]
