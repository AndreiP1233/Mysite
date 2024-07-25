from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from users.forms import LoginUserForm, RegUserForm

# import logging

# logger = logging.getLogger(__name__)

def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegUserForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            authenticated_user = auth.authenticate(username=new_user.username,
                                              password=request.POST['password'])
            auth.login(request, authenticated_user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form=RegUserForm()
    return render(request, 'users/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def profile(request):
    return render(request, 'users/profile.html')

