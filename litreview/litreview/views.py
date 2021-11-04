from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from forms import UserRegisterForm


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'litreview/user/register.html'
    success_url = reverse_lazy('follows')
    form_class = UserRegisterForm
    success_message = "Votre inscription est prise en compte merci de vous connecter"


def index(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is None:
            context = {
                "error": "Invalid password or username",
                "form": form}
            return render(request, "litreview/index.html", context)
        login(request, user)
    return render(request, "litreview/index.html", context={"form": form})


def disconnect(request):
    logout(request)
    return redirect('home')
