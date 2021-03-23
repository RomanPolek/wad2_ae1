from django.db import models
from django.utils.translation import gettext_lazy as _


# User of the website, either Student or Teacher
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()

    class Role(models.TextChoices):
        STUDENT = 'Student', _('Student')
        TEACHER = 'Teacher', _('Teacher')

    role = models.CharField(
        max_length=7, choices=Role.choices, default=Role.STUDENT
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Course taken by many Students and taught by one (more than one?) Teacher
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='taught', null=True, blank=True)
    students = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"


# Question to be asked as part of an exam
class Question(models.Model):
    # the actual text/content of the question
    content = models.CharField(max_length=250)
    # TODO: probably there'll be some checks needed but hey, variable numbers of choices are coool
    choice_1 = models.CharField(max_length=300, blank=True)
    choice_2 = models.CharField(max_length=300, blank=True)
    choice_3 = models.CharField(max_length=300, blank=True)
    choice_4 = models.CharField(max_length=300, blank=True)
    choice_5 = models.CharField(max_length=300, blank=True)
    # id of the correct answer (1 - 5)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f"{self.content}"


# Exam taken by a student
# Questions are added to it using a many-to-many field
class Exam(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_available = models.DateTimeField()
    deadline = models.DateTimeField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"{self.title} ({self.course})"


# Answer given by a student while taking the exam, used for marking
class Answer(models.Model):
    # question the answer is attached to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # id of the answer given by the student, to be compared with Question's answer field
    answer = models.IntegerField()

    def __str__(self):
        return f"{self.question} - {self.answer}"


# Result of an exam taken by a student
# Created when the students starts the exam
# Answers to questions are added to it
# Score can be calculated by accessing answers
# Used by Teachers for marking
class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return f"{self.exam} ({self.student})"
