from django.urls import path
from . import views

app_name = 'exam_network'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('welcome_back/', views.welcome_back, name='welcome_back'),
]
