from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .models import Exam, Course, Question

def index(request):
    return render(request, 'exam_network/index.html', {})


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
        return HttpResponse("Invalid login details supplied.")
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


def error(request, message, error):
    return render(request, 'exam_network/error.html', status=error, context={"message": message, "error": error})


##Added by Roman. You can modify these views. I just used them for frontend development##
def signup(request):
    if request.user.is_authenticated:
        return error(request, "you are already logged in", 403)
    elif request.method == "POST":
        print(request.POST)
    else:
        return render(request, 'exam_network/signup.html')

def welcome_back(request):
    return render(request, 'exam_network/welcome_back.html')

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
##Added by Roman. You can modify these views. I just used them for frontend development##