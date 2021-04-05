from django import template
from exam_network.models import Submission
register = template.Library()


@register.simple_tag
def get_answer(l, question):
    return l.get(question=question).answer
    
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