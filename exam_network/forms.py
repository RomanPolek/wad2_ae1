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

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError(
                ('Password too short.'),
                code='invalid_password_len',
            )
        return password

    def clean_conform_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("conform_password")
        if password1 != password2:
            raise forms.ValidationError(
                ('Password mismatch.'),
                code='password_mismatch',
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count() != 0:
            raise forms.ValidationError(
                ("This email is already in use."),
                code='email_in_use',
            )
        return email


class ProfileForm(forms.ModelForm):
    ROLES = [('S', 'Student'), ('T', 'Teacher')]
    role = forms.ChoiceField(
            choices=ROLES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('role',)

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role != 'S' and role != 'T':
            raise forms.ValidationError(
                ("Invalid role."),
                code='invalid_role',
            )
        return role
