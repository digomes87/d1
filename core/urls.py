from django.urls import path, include
from .views import index, contato

urlpatterns = [
    path('', index),
    path('contato', contato)
]
