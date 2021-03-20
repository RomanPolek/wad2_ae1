from django.shortcuts import render, redirect


def index(request):
    return render(request, 'exam_network/index.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('exam_network:index'))
            return HttpResponse("Your Exam Network account is disabled.")
        print(f'Invalid login details: {username}')
        return HttpResponse("Invalid login details supplied.")
    else:
        # TODO: check the names of html files when available
        return render(request, 'exam_network/login.html')

def contact(request):
    return render(request, 'exam_network/contact.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('exam_network:index'))

def show_exams(request, course_name):
    context_dict = {}
    try:
        course = Course.objects.get(name=course_name)
        exams = Exam.objects.filter(course=course)
        context_dict['course'] = course
        context_dict['exams'] = exams

    except Category.DoesNotExist:
        context_dict['course'] = None
        context_dict['exams'] = None
    # TODO: check the names of html files when available
    return render(request, 'exam_network/exam.html', context=context_dict)

def handler404(request, exception):
        return render(request, 'exam_network/handler404.html', status=404)
