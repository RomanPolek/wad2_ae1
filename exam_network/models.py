from django.db import models

# TODO: some foreign keys are missing
# TODO: user-related models


# Course taken by many Students and taught by one (more than one?) Teacher
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


# Exam taken by a student
# Questions are added to it using a many-to-many field
class Exam(models.Model):
    date_available = models.DateTimeField()
    deadline = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


# Result of an exam taken by a student
# Created when the students starts the exam
# Answers to questions are added to it
# Score can be calculated by accessing the answer set
# Used by Teachers for marking
class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)


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
    answer = models.IntegerField()


# Answer given by a student while taking the exam, used for marking
class Answer(models.Model):
    # result the question belongs to
    result = models.ManyToManyField(Result)
    # id of the answer given by the student, to be compared with Question's answer field
    answer = models.IntegerField()
    # question the answer is attached to
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
