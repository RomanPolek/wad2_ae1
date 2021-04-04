from django import forms
from django.contrib.auth.models import User
import datetime
from exam_network.models import Profile, Course, Question, Exam, Answer, Submission


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"class": "input_row", "placeholder": "Enter First Name"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"class": "input_row", "placeholder": "Enter Last Name"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={"class": "input_row", "placeholder": "Enter Email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "input_row", "placeholder": "Enter Password"}))
    conform_password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "input_row", "placeholder": "Re-enter Password"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',)


class ProfileForm(forms.ModelForm):
    ROLES = [('S', 'Student'), ('T', 'Teacher')]
    role = forms.ChoiceField(
            choices=ROLES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('role',)
