from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from long_link_reduction_service_app.forms import RegisterUserForm, LoginUserForm


def index(request):
    return render(request, "index.html")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')




def logout_user(request):
    logout(request)
    return redirect('home')