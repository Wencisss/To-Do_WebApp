
from django.urls import path

from . import views

app_name = 'toDoApp'
urlpatterns = [
    path('', views.home, name='home'),
]
