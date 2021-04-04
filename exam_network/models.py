from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4().hex, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Role(models.TextChoices):
        STUDENT = ('S', 'Student')
        TEACHER = ('T', 'Teacher')

    role = models.CharField(
        max_length=1, choices=Role.choices, default=Role.STUDENT)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Course taken by many Students and taught by one (more than one?) Teacher
class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=50)
    authorised = models.ManyToManyField(User)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


# Exam taken by a student
# Questions are added to it using a many-to-many field
class Exam(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_available = models.DateTimeField()
    deadline = models.DateTimeField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} ({self.course})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


# Question to be asked as part of an exam
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
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


# Submission of an exam taken by a student
# Created when the students starts the exam
# Answers to questions are added to it
# Score can be calculated by accessing answers
# Used by Teachers for marking
class Submission(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.exam} ({self.student})"


# Answer given by a student while taking the exam, used for marking
class Answer(models.Model):
    exam = models.ForeignKey(Submission, on_delete=models.CASCADE)
    # question the answer is attached to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # id of the answer given by the student, to be compared with Question's answer field
    answer = models.IntegerField()

    def __str__(self):
        return f"{self.question} - {self.answer}"
