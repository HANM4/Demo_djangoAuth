from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('user_account:profile')


@login_required
def profile_view(request):
    return render(request, 'profile.html')


class SignupUser(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user_account:profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
