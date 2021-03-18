from django.urls import path
from . import views

app_name = 'exam_network'

urlpatterns = [
    path('', views.index, name='index'),
]
