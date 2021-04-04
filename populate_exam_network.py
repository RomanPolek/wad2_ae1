import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'exam_network.settings')
import django
from django.contrib.auth.models import User
from exam_network.models import Profile
django.setup()


def populate():
    teachers = []
    students = []
    courses = []
    exams = []
    results = []


def add_user(first_name, last_name, email, password):
    u = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password)
    return u


def add_profile(user, role):
    prof = Profile.objects.create(
        user=user, role=role)
    return prof


def add_course():
    pass


def add_exam():
    pass


def add_result():
    pass


if __name__ == "__main__":
    print('Starting Exam Network population script...')
    populate()
