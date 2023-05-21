from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'riddles'

urlpatterns = [
    path("index/", views.index, name='index'),
]
