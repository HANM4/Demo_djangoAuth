from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator


def login_view(request):
    error = None
    # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('user_account:profile'))
                else:
                    error = 'The account has been disabled.'
            else:
                error = 'The username and/or password is incorrect.'
        else:
            error = 'The username and/or password is don`t valid.'
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def profile_view(request):
    return render(request, 'profile.html')


# add this function
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('user_account:profile'))
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})