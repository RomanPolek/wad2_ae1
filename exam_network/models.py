from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import uuid


class Profile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)

    class Role(models.TextChoices):
        STUDENT = ('S', 'Student')
        TEACHER = ('T', 'Teacher')
        NONE = ('N', 'None')

    role = models.CharField(
        max_length=1, choices=Role.choices, default=Role.NONE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.role})"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Course taken by many Students and taught by one (more than one?) Teacher
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='taught', null=True, blank=True)
    students = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"


# Question to be asked as part of an exam
class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # the actual text/content of the question
    content = models.CharField(max_length=250)
    # TODO: probably there'll be some checks needed but hey, variable numbers of choices are coool
    choice_0 = models.CharField(max_length=300, blank=True)
    choice_1 = models.CharField(max_length=300, blank=True)
    choice_2 = models.CharField(max_length=300, blank=True)
    choice_3 = models.CharField(max_length=300, blank=True)
    choice_4 = models.CharField(max_length=300, blank=True)
    # id of the correct answer (0 - 4)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f"{self.content}"


# Exam taken by a student
# Questions are added to it using a many-to-many field
class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_available = models.DateTimeField()
    deadline = models.DateTimeField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"{self.title} ({self.course})"


@receiver(pre_delete, sender=Exam)
def pre_delete_exam(sender, instance, **kwargs):
    for question in list(instance.questions.all()):
        if question.exam_set.count() == 1:
            question.delete()


# Answer given by a student while taking the exam, used for marking
class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # question the answer is attached to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # id of the answer given by the student, to be compared with Question's answer field
    answer = models.IntegerField()

    def __str__(self):
        return f"{self.question} - {self.answer}"


# Submission of an exam taken by a student
# Created when the students starts the exam
# Answers to questions are added to it
# Score can be calculated by accessing answers
# Used by Teachers for marking
class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    max_score = models.IntegerField()
    answers = models.ManyToManyField(Answer)
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.exam} ({self.student})"


@receiver(post_save, sender=Exam)
def update_submission_scores(sender, instance, created, **kwargs):
    max_score = len(instance.questions.all())
    questions = {str(q.content) for q in list(instance.questions.all())}

    submissions = Submission.objects.filter(exam=instance)
    for submission in submissions:
        score = 0

        old_answers = list(submission.answers.all())
        for answer in old_answers:
            # question wasn't deleted, increase score if answer was correct
            if str(answer.question.content) in questions:
                print('answers', answer.answer, answer.question.correct_answer)
                if answer.answer == answer.question.correct_answer:
                    score += 1
            else:
                submission.answers.remove(answer)

        submission.score = score
        submission.max_score = max_score
        submission.percentage = round(score / max_score * 10000) / 100
        submission.save()
