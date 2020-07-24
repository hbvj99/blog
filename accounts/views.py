from django.shortcuts import render, redirect
from accounts.forms import CreateUser


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
    if request.method == 'POST':
        user_form = CreateUser(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()
            return redirect('/')
    else:
        user_form = CreateUser()
    context = {'user_form': user_form}
    return render(request, 'accounts/signup.html', context)
