from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


# TODO: view isn't used anywhere
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('main_page:index'))
            return HttpResponse("Your Exam Network account is disabled.")

        print(f'Invalid login details: {username}, {password}')
        return HttpResponse("Invalid login details supplied.")
    else:
        # TODO: template doesn't exist yet but very much should
        return render(request, 'exam_network/login.html')
