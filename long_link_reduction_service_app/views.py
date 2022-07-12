from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from long_link_reduction_service_app.forms import RegisterUserForm, LoginUserForm

from .models import Reducer



from .forms import ReducerForm


# def index(request):
#     return render(request, "index.html")


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




def home_view(request):
    template = 'index.html'

    context = {}


    context['form'] = ReducerForm()

    if request.method == 'GET':

        return render(request, template, context)

    elif request.method == 'POST':

        # used_form = ReducerForm(request.POST)
        user_form = ReducerForm(request.POST)

        # user_id = request.user
        # if used_form.is_valid():
        #     reducer_object = used_form.save()
        if user_form.is_valid():

            # user_id = request.user

            reducer_object = user_form.save()

            new_url = request.build_absolute_uri('/') + reducer_object.modified_url

            origin_url = reducer_object.origin_url

            context['new_url'] = new_url
            context['origin_url'] = origin_url




            return render(request, template, context)

        context['errors'] = user_form.errors

        return render(request, template, context)




def redirect_url_view(request, shortened_part):
    try:
        shortener = Reducer.objects.get(modified_url=shortened_part)



        shortener.save()

        return HttpResponseRedirect(shortener.origin_url)

    except:
        raise Http404('Sorry this link is broken :(')

