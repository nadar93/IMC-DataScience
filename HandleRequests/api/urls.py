from django.urls import path
from .views import handleRequest
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #path('', handleRequest),
    path('', csrf_exempt(handleRequest)),
]