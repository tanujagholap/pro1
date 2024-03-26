from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



def user_login(request):
    template_name = 'app2/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_urls')
        else:
            return HttpResponse('plz enter correct username')
    return render(request, template_name)


def user_logout(request):
    logout(request)
    return redirect('login_urls')


def sign_up(request):
    template_name = 'app2/register.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration Success')
    return render(request, template_name, context={'form': form})


@login_required(login_url='login_urls')
def change_password(request):
    if request.method == 'POST':
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_urls')
        return render(request, 'app2/cpass.html')

