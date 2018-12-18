from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from GUI.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('dashboard/', include('GUI.urls'))
]