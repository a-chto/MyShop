from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from .forms import UserRegisterForm, UserLoginForm
from .models import User


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                send_verify_email(user)
            return redirect('main:main')
        else:
            return render(request, 'custom_auth/register.html', {'form': form})
    elif request.method == "GET":
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'custom_auth/register.html', context)


def send_verify_email(user):
    """
    отправка письма пользователю с подтверждением
    """
    if user.is_active:
        # пользователь уже активен
        pass
    link = user.activation_code
    title = f' Подтверждение {user.email}'
    body = f'Для активации перейдите по ссылке {link}'
    send_mail(title, body, settings.DEFAULT_FROM_EMAIL, [user.email])

    
def verify_user(request, email, activation_code):
    try:
        user = User.objects.get(email = email)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('main:main'))