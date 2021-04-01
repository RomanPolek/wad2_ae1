from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .models import Exam, Course, Question
from django.contrib.auth.models import User
from django.contrib.auth import login

def error(request, message, error):
    return render(request, 'exam_network/error.html', status=error, context={"message": message, "error": error})

def index(request):
    return render(request, 'exam_network/index.html', {})

def signup(request):
    if request.user.is_authenticated:
        return error(request, "you are already logged in", 403)
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("email")
        role = request.POST.get("role")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        #checks
        if password != confirm_password:
            return error(request, "the passwords do not match", 403)
        if password == None or password.strip() == "":
            return error(request, "the password is empty", 403)
        if role != "S" and role != "T":
            return error(request, "the role is invalid", 403)
        if role != "S" and role != "T":
            return error(request, "the role is invalid", 403)
        if email == None or email.strip() == "":
            return error(request, "the email is empty", 403)
        if last_name == None or last_name.strip() == "":
            return error(request, "the surname is empty", 403)
        if first_name == None or first_name.strip() == "":
            return error(request, "the name is empty", 403)
        
        #passed checks
        user,_ = User.objects.get_or_create(username=username)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.profile.role = role
        login(request, user)
        return render(request, 'exam_network/welcome.html')
    else:
        return render(request, 'exam_network/signup.html')

def user_login(request):
    if request.user.is_authenticated:
        return error(request, "you are already logged in", 403)
    elif request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('exam_network:index'))
            return HttpResponse("Your Exam Network account is disabled.")
        print(f'Invalid login details: {username}')
        return error(request, "the login details are incorrect", 403)
    else:
        return render(request, 'exam_network/login.html')


def contact(request):
    return render(request, 'exam_network/contact.html')


def user_logout(request):
    if not request.user.is_authenticated:
        return error(request, "you are not logged in", 403)
    else:
        logout(request)
        return redirect(reverse('exam_network:index'))


def show_exams(request, course_name):
    context_dict = {}
    try:
        course = Course.objects.get(name=course_name)
        exams = Exam.objects.filter(course=course)
        context_dict['course'] = course
        context_dict['exams'] = exams

    except Course.DoesNotExist:
        context_dict['course'] = None
        context_dict['exams'] = None
    return render(request, 'exam_network/exams.html', context=context_dict)


def show_exam(request, exam_name):
    context_dict = {}
    try:
        # TODO: modify the ER Diagram and models to include exam name
        exam = Exam.objects.get(exam=exam_name)
        questions = Question.objects.filter(exam=exam)
        context_dict['exam'] = exam
        context_dict['questions'] = questions

    except Exam.DoesNotExist:
        context_dict['exams'] = None
        context_dict['questions'] = None
    return render(request, 'exam_network/exam.html', context=context_dict)

def add_course(request):
    return render(request, 'exam_network/add_course.html')

def add_students(request):
    return render(request, 'exam_network/add_students.html')

def about_us(request):
    return render(request, 'exam_network/about_us.html')

def exam_result(request):
    return render(request, 'exam_network/exam_result.html')

def exams(request):
    return render(request, 'exam_network/exams.html')

def exam(request, slug):
    return render(request, 'exam_network/exam.html')

def help(request):
    return render(request, 'exam_network/help.html')

def welcome(request):
    return render(request, 'exam_network/welcome.html')