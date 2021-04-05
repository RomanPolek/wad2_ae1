from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .models import Exam, Course, Question
from django.contrib.auth.models import User
from django.db.models import Q
import datetime
from django.utils.timezone import make_aware


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

    # checks
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

    # passed checks
    user = None
    if create:
        try:
            User.objects.get(username=username)  # check if this user exists
            return error(request, "this email is already taken", 403)
        except:
            # doesnt exist so create
            user = User.objects.create(username=username)
    else:
        try:
            # check if this user exists
            user = User.objects.get(username=username)
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


def get_courses(request):
    if not request.user.is_authenticated:
        return Course.objects.none()
    if request.user.profile.role == "S":
        return Course.objects.filter(students__in=[request.user])
    elif request.user.profile.role == "T":
        return Course.objects.filter(teacher=request.user)
    else:
        return Course.objects.none()


def get_exams(courses):
    now = datetime.datetime.now()
    return Exam.objects.filter(course__in=courses, deadline__gte=now).order_by("date_available")


def signup(request):
    if request.user.is_authenticated:
        return error(request, "you are already logged in", 403)
    elif request.method == "POST":
        return process_account_edit(request, 'welcome', True)
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


def account(request):
    if not request.user.is_authenticated:
        return error(request, "you are not logged in", 403)
    elif request.method == 'POST':
        return process_account_edit(request, 'index', False)
    else:
        return render(request, 'exam_network/account.html')


def contact(request):
    return render(request, 'exam_network/contact.html')


def user_logout(request):
    if not request.user.is_authenticated:
        return error(request, "you are not logged in", 403)
    else:
        logout(request)
        return redirect(reverse('exam_network:index'))

def add_course(request):
    if not request.user.is_authenticated:
        return error(request, "you are not logged in", 403)
    elif request.user.profile.role != "T":
        return error(request, "you do not have permission do perform this operation", 403)
    elif request.method == 'POST':
        # get data
        name = request.POST.get('course_name')
        details = request.POST.get('details')

        # perform checks
        if name == None or name.strip() == "":
            return error(request, "the course name is not filled in", 403)
        if details == None or details.strip() == "":
            return error(request, "the details are not filled in", 403)

        # create new course if successful and if does not exist
        try:
            Course.objects.get(name__eq=name)  # check if already exists
            return error(request, "a course with this name already exists", 403)
        except:
            course = Course.objects.create(
                name=name, description=details, teacher=request.user)
            course.save()
        return redirect(reverse('exam_network:index'))
    else:
        return render(request, 'exam_network/add_course.html')


def add_students(request):
    courses = get_courses(request)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return error(request, "you are not logged in", 403)
        elif request.user.profile.role != "T":
            return error(request, "you do not have permission to add students", 403)
        else:
            try:
                course = courses.get(id=request.POST.get(
                    "course_id"), teacher=request.user)
                students = request.POST.get("students").split(",")
                excluded_students = []
                for student in students:
                    student = student.strip()
                    try:
                        student_object = User.objects.get(email=student)
                        if student_object.profile.role != "S":
                            # gets catched in except
                            raise Exception("user is not a student")
                        if student_object in course.students.all():
                            # gets catched in except
                            raise Exception("user is already in the course")
                        if student_object == course.teacher:
                            # gets catched in except
                            raise Exception("user is a teacher")

                        course.students.add(student_object)
                    except:
                        excluded_students.append(student)

                if len(excluded_students) == len(students):
                    return error(request, "the operation was not successful. None of these students were added: " + ", ".join(excluded_students), 403)
                if len(excluded_students) != 0:
                    return error(request, "the operation was succesfull but these students were not added: " + ", ".join(excluded_students), 0)
                else:
                    return redirect(reverse('exam_network:exams'))
            except:
                return error(request, "you do not have permission to add students into this course", 403)
    else:
        return render(request, 'exam_network/add_students.html', {"courses": get_courses(request)})


def get_datetime(datetime_string):
    result = datetime.datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M")
    # expecting that all the times will be in UTC timezone
    return make_aware(result)


def add_exam(request):
    if request.method == "POST":
        courses = get_courses(request)
        if not request.user.is_authenticated:
            return error(request, "you are not logged in", 403)
        elif request.user.profile.role != "T":
            return error(request, "you do not have permission to add exam", 403)
        else:
            try:
                course = courses.get(id=request.POST.get("course_id"))
                title = request.POST.get("title")
                date_available = get_datetime(
                    request.POST.get("date_available"))
                deadline = get_datetime(request.POST.get("deadline"))

                now = make_aware(datetime.datetime.now())
                try:
                    Exam.objects.get(title=title)  # check if exists
                    return error(request, "exam with this name already exists", 403)
                except:
                    pass
                if title == None or title.strip() == "":
                    return error(request, "the exam title is emty", 403)
                if deadline < date_available:
                    return error(request, "the deadline of the exam is before date available", 403)
                if deadline < now:
                    return error(request, "the deadline of the exam is in the past", 403)

                exam = Exam.objects.create(
                    title=title, course=course, date_available=date_available, deadline=deadline)

                # get questions
                counter = 0
                while True:
                    if ("question_" + str(counter)) in request.POST:
                        question = Question.objects.create(
                            content=request.POST.get(
                                "question_" + str(counter)),
                            choice_0=request.POST.get(
                                "answer_" + str(counter) + "_0"),
                            choice_1=request.POST.get(
                                "answer_" + str(counter) + "_1"),
                            choice_2=request.POST.get(
                                "answer_" + str(counter) + "_2"),
                            choice_3=request.POST.get(
                                "answer_" + str(counter) + "_3"),
                            choice_4=request.POST.get(
                                "answer_" + str(counter) + "_4"),
                            correct_answer=int(request.POST.get(
                                "correct_answer_" + str(counter)))
                        )
                        question.save()
                        exam.questions.add(question)
                        counter += 1
                    else:
                        break
                exam.save()
                return redirect(reverse('exam_network:exams'))
            except:
                return error(request, "you do not have permission to add exam into this course", 403)
    else:
        return render(request, 'exam_network/add_exam.html', {"courses": get_courses(request)})


def about_us(request):
    return render(request, 'exam_network/about_us.html')


def exam_result(request):
    return render(request, 'exam_network/exam_result.html')


def exams(request, id=None):
    # get the available exams
    courses = get_courses(request)
    exams = get_exams(courses)
    current_course = False
    now = make_aware(datetime.datetime.now())
    if not request.user.is_authenticated:
        return error(request, "you are not logged in", 403)
    elif len(exams.filter(id=id)) != 0:
        # this id is an exam
        exam = None
        try:
            exam = exams.get(id=id, date_available__lte=now, deadline__gt=now)
        except:
            return error(request, "this exam does not exist", 403)

        if request.method == "POST":
            #received submission
            counter = 0
            score = 0
            max_score = len(exam.questions.all())
            choices = []
            while True:
                if ("question_" + counter) in request.POST:
                    current = request.POST.get("question_" + counter)
                    if current == exam.questions.all()[counter].correct_answer:
                        score += 1
                    choices.append(current)
                    counter += 1
                else:
                    break
            return render(request, 'exam_network/exam.html', {"exam": exam, "choices": choices, "score": score, "max_score": max_score})
        else:
            return render(request, 'exam_network/exam.html', {"exam": exam})

    # if the id is course filter exams based on this course
    try:
        current_course = courses.get(id=id)
        exams = exams.filter(course=current_course)
    except:
        pass

    context_dict = {"courses": courses, "exams": exams,
                    "user_role": request.user.profile.role,
                    "current_course": current_course, "now": now}

    return render(request, 'exam_network/exams.html', context_dict)


def help(request):
    return render(request, 'exam_network/help.html')


def welcome(request):
    # TODO: Should be a different message for students & teachers
    return render(request, 'exam_network/welcome.html')
