from django.urls import path
from . import views

app_name = 'exam_network'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_students/', views.add_students, name='add_students'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('exam_result/', views.exam_result, name='exam_result'),
    path('help/', views.help, name='help'),
    path('account/', views.account, name='account'),
    path('exams/', views.exams, name='exams'),
    path('exams/<id>', views.exams, name='exams'),
]
