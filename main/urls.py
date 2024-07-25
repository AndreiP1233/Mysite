from django.urls import path, include
from django.contrib import admin

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
