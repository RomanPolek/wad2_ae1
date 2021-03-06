from django import template
from exam_network.models import Submission, Exam
from django.contrib.auth.models import User
register = template.Library()


@register.simple_tag
def get_answer(l, question):
    try:
        return l.get(question=question).answer
    except:
        return -1
    
@register.filter(name='times') 
def times(number):
    return range(number)

@register.simple_tag
def get_submission(user, exam):
    try:
        if user.profile.role != "S":
            raise Exception("user is not student")
        return Submission.objects.get(student=user, exam=exam)
    except:
        return None

@register.simple_tag
def get_all_submission(exam):
    try:
        return Submission.objects.filter(exam=exam)
    except:
        return None

def round_two_decimal(x):
    return round(x * 100) / 100

@register.simple_tag
def get_student_performance(user, course):
    submissions = None
    if course:
        submissions = Submission.objects.filter(student=user, exam__in=Exam.objects.filter(course=course))
    else:
        submissions = Submission.objects.filter(student=user)
    maximum = 0.0
    minimum = 100.0
    average = 0.0
    for submission in submissions:
        if submission.percentage > maximum:
            maximum = submission.percentage
        if submission.percentage < minimum:
            minimum = submission.percentage
        average += submission.percentage
    if len(submissions) > 0:
        average /= len(submissions)
    else:
        minimum = 0
    
    return [round_two_decimal(maximum), round_two_decimal(minimum), round_two_decimal(average)]

@register.simple_tag
def get_course_performance(course):
    course_performance = [0.0,100.0,0.0,0]
    for student in course.students.all():
        current = get_student_performance(student, course)
        if current[0] > course_performance[0]:
            course_performance[0] = current[0]
        if current[1] < course_performance[1]:
            course_performance[1] = current[1]
        course_performance[2] += current[2]
    course_performance[3] = len(course.students.all())
    if course_performance[3] > 0:
        course_performance[2] /= course_performance[3]

    course_performance[0] = round_two_decimal(course_performance[0])
    course_performance[1] = round_two_decimal(course_performance[1])
    course_performance[2] = round_two_decimal(course_performance[2])
    return course_performance

@register.simple_tag
def exam_display_result(user, user_choice):
    return (user_choice != "" or user.profile.role == 'T') and user_choice != -1