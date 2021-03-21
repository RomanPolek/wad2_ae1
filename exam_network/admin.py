from django.contrib import admin
from django import forms
from exam_network.models import Course, User, Exam, Result, Question, Answer


class UserAdminForm(forms.ModelForm):
    course_set = forms.ModelMultipleChoiceField(
        label='Courses', queryset=Course.objects.all(), required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name='Courses',
            is_stacked=False
        )
    )

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            # Depending on the Role, the Course field should be either Courses taken or taught
            # Set the initial field value to either 'course_set' for Students or 'taught' for Teachers
            if self.instance.role == 'Student':
                self.fields['course_set'].initial = self.instance.course_set.all()
            else:
                self.fields['course_set'].initial = self.instance.taught.all()

            # Adjust the label depending on the role
            self.fields['course_set'].label += ' taken' if self.instance.role == 'Student' else ' taught'

    def save(self, commit=True):
        user = super(UserAdminForm, self).save(commit=False)

        if commit:
            user.save()

        if user.pk:
            # If changes were made we need to save them to the right field depending on the Role
            if self.instance.role == 'Student':
                user.course_set.set(self.cleaned_data['course_set'])
            else:
                user.taught.set(self.cleaned_data['course_set'])

            self.save_m2m()

        return user


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')
    form = UserAdminForm
    fields = ['first_name', 'last_name', 'email', 'role', 'course_set']


class CourseAdminForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        # Filters out Teachers from the Student picker
        label='Students', queryset=User.objects.filter(role='Student'),
        required=False,
        widget=admin.widgets.FilteredSelectMultiple(
            verbose_name='Students',
            is_stacked=False
        )
    )

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['students'].initial = self.instance.students.all()

    def save(self, commit=True):
        course = super(CourseAdminForm, self).save(commit=False)

        if commit:
            course.save()

        if course.pk:
            course.students.set(self.cleaned_data['students'])
            self.save_m2m()

        return course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    form = CourseAdminForm
    fields = ['name', 'description', 'teacher', 'students']

    # Filter out Students from the Teacher dropdown
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(role='Teacher')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'date_available', 'deadline')


# TODO: do we need exams the question is added to or not?
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'choices', 'correct_answer')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student')

    # Filter out teachers from the Student dropdown
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "student":
            kwargs["queryset"] = User.objects.filter(role='Student')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(Course, CourseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
