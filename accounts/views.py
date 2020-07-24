from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import CreateUser, UserDetail


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


@login_required()
def update_profile(request):
    if request.method == 'POST':
        form = UserDetail(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserDetail(instance=request.user)
        return render(request, 'accounts/update_profile.html', {'form': form})
