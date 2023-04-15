from django.shortcuts import render

from .forms import UserRegisterForm, UserLoginForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                pass
    elif request.method == "GET":
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'custom_auth/register.html', context)