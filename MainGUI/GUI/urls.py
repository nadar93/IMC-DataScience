from django.conf.urls import url
from .views import Dashboard

urlpatterns = [
    url('', Dashboard.as_view(), name='dashboard'),
]