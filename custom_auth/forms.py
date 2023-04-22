from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name', 'password1', 'password2')
        def save(self, *args, **kwargs):
            user = super().save(*asrgs, **kwargs)
            return user

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')