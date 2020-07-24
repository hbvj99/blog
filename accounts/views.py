from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.forms import CreateUser, UserDetail

UserModel = get_user_model()


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your new account'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/signup_confirmation.html')
    else:
        form = CreateUser()
    context = {'user_form': form}
    return render(request, 'accounts/signup.html', context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponseNotFound('Error! Not a valid request')


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
