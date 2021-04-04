from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .models import Exam, Course, Question, Profile, Submission
from .forms import UserForm, ProfileForm, ExamForm, QuestionForm
from django.contrib.auth.models import User
from django.db.models import Q
import datetime

def error(request, message, error):
    return render(request, 'exam_network/error.html', status=error, context={"message": message, "error": error})

def index(request):
    return render(request, 'exam_network/index.html', {})

def process_account_edit(request, return_url_name, create):
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
    user = None
    if create:
        try:
            User.objects.get(username__eq=username) #check if this user exists
            return error(request, "this email is already taken", 403)
        except:
            user = User.objects.create(username=username) #doesnt exist so create
    else:
        try:
            user = User.objects.get(username=username) #check if this user exists
        except:
            return error(request, "this account does not exist", 403)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    if password != "***********":
        user.set_password(password)
    user.profile.role = role
    user.save()
    login(request, user)
    return redirect(reverse('exam_network:' + return_url_name))


def signup(request):
    context_dict = {}
    is_registered = False
    if request.user.is_authenticated:
        return error(request, "you are already logged in", 403)
    user_form = None
    profile_form = None
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            is_registered = True
            login(request, user)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    context_dict["user_form"] = user_form
    context_dict["profile_form"] = profile_form
    context_dict['registered'] = is_registered
    return render(request, 'exam_network/signup.html', context_dict)


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


@login_required
def account(request):
    if request.method == 'POST':
        return process_account_edit(request, 'index', False)
    else:
        return render(request, 'exam_network/account.html')


@login_required
def user_logout(request):
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

def show_submissions(request, course_name):
    context_dict = {}
    try:
        course = Course.objects.get(name=course_name)
        exams = Exam.objects.filter(course=course)
        submissions = Submission.objects.filter(student=request.user).filter(exam=exams)
        context_dict['submissions'] = submissions
    except Course.DoesNotExist:
        context_dict['submissions'] = None
    return render(request, 'exam_network/results.html', context=context_dict)

def add_course(request):
    if not request.user.is_authenticated:
        return error(request, "you are not logged in", 403)
    elif request.user.profile.role != "T":
        return error(request, "you do not have permission do perform this operation", 403)
    elif request.method == 'POST':
        #get data
        name = request.POST.get('course_name')
        details = request.POST.get('details')

        #perform checks
        if name == None or name.strip() == "":
            return error(request, "the course name is not filled in", 403)
        if details == None or details.strip() == "":
            return error(request, "the details are not filled in", 403)

        #create new course if successful and if does not exist
        try:
            Course.objects.get(name__eq=name) #check if already exists
            return error(request, "a course with this name already exists", 403)
        except:
            course = Course.objects.create(name=name, description=details, teacher=request.user)
            course.save()
        return redirect(reverse('exam_network:index'))
    else:
        return render(request, 'exam_network/add_course.html')


@login_required
def add_students(request):
    context_dict = {'course_form_error': None, 'student_form_error': None}
    if(request.user.profile.role != 'T'):
        return error(request, "Unauthorised Access.", 401)
    context_dict['courses'] = Course.objects.filter(authorised=request.user)
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        email = request.POST.get('student_email')
        try:
            course = Course.objects.get(name=course_name)
            student = User.objects.get(email=email)
            course.authorised.add(student)
        except Course.DoesNotExist:
            context_dict['course_form_error'] = "Invalid Course."
        except User.DoesNotExist:
            context_dict['student_form_error'] = "Invalid Student Email."
    return render(request, 'exam_network/add_students.html', context_dict)


@login_required
def add_exam(request):
    if(request.user.profile.role != 'T'):
        return error(request, "Unauthorised Access.", 401)
    context_dict = {}
    is_completed = False
    exam_form = None
    courses = Course.objects.filter(authorised=request.user)
    context_dict['courses'] = courses
    if request.method == 'POST':
        exam_form = ExamForm(request.POST)
        if exam_form.is_valid():
            exam = exam_form.save()
            course_name = request.POST.get("course_name")
            course = Course.objects.get(name=course_name)
            exam.course = course
            exam.save()
            is_completed = True
    else:
        exam_form = ExamForm()
    context_dict['completed'] = is_completed
    context_dict['exam_form'] = exam_form
    return render(request, 'exam_network/add_exam.html', context_dict)


@login_required
def exam_result(request, course_slug_name, exam_slug_name):
    context_dict = {}
    try:
        courses = Course.objects.filter(authorised=request.user)
        context_dict['courses'] = courses
        course = courses.objects.get(slug=course_slug_name)
        context_dict['course'] = course
        exam = Exam.objects.get(course=course, slug=exam_slug_name)
        submission = Submission.objects.get(exam=exam, student=request.user)
        context_dict['submission'] = submission
    except Course.DoesNotExist:
        context_dict['course'] = None
    except Submission.DoesNotExist:
        context_dict['submission'] = None
    return render(request, 'exam_network/exam_result.html')


@login_required
def exams(request, course_slug_name):
    context_dict = {}
    try:
        courses = Course.objects.filter(authorised=request.user)
        context_dict['courses'] = courses
        course = courses.objects.get(slug=course_slug_name)
        context_dict['course'] = course
        now = datetime.datetime.now()
        exams = Exam.objects.filter(
            course=course,
            date_available__lte=now,
            deadline__gte=now)
        context_dict['exams'] = exams
    except Course.DoesNotExist:
        context_dict['course'] = None
        context_dict['exams'] = None
    return render(request, 'exam_network/exams.html', context_dict)


def contact(request):
    return render(request, 'exam_network/contact.html')


def about_us(request):
    return render(request, 'exam_network/about_us.html')


def help(request):
    return render(request, 'exam_network/help.html')


def welcome(request):
    return render(request, 'exam_network/welcome.html')
