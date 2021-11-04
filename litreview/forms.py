from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={"placeholder": "Nom utilisateur"}),
            'password1': PasswordInput(attrs={"placeholder": "Mot de passe"}),
            'password2': PasswordInput(attrs={"placeholder": "Répéter Mot de passe"}),
        }
