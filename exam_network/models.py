from django.db import models
from django.utils.translation import gettext_lazy as _

# TODO: some foreign keys are missing


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
        return f"{self.first_name} {self.last_name} ({self.id})"


# Course taken by many Students and taught by one (more than one?) Teacher
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='taught', null=True, blank=True)
    students = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name}"


# Exam taken by a student
# Questions are added to it using a many-to-many field
class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_available = models.DateTimeField()
    deadline = models.DateTimeField()


# Result of an exam taken by a student
# Created when the students starts the exam
# Answers to questions are added to it
# Score can be calculated by accessing the answer set
# Used by Teachers for marking
class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)


# Question to be asked as part of an exam
# TODO: potentially an imagefield to add images as part of the question? not v needed, could do
class Question(models.Model):
    # exam the question belongs to
    exam = models.ManyToManyField(Exam)
    # the actual text/content of the question
    content = models.CharField(max_length=250)
    # TODO: probably there'll be some checks needed but hey, variable numbers of choices are coool
    choices = models.JSONField()
    # id of the correct answer
    # alternatively could use another JSONField if we allow more than one correct answer
    correct_answer = models.IntegerField()


# Answer given by a student while taking the exam, used for marking
class Answer(models.Model):
    # result the question belongs to
    result = models.ManyToManyField(Result)
    # id of the answer given by the student, to be compared with Question's answer field
    answer = models.IntegerField()
    # question the answer is attached to
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
