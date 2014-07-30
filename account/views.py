from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import random

from .forms import AccountCreateForm, AccountAuthForm
from core.views import index
from utils.func import *

########################
# View profile
########################

@login_required
def view_profile(request): #, search_query=""):
    #form = EventForm(data=request.POST or None, user=request.user)
    template = 'account/view_profile.html'

    try:
        user_id = request.GET.get('user_id','')
        student = Account.objects.get(user__username=user_id)
    except:
        student = None
        pass

    return render(request,
                  template,
                  {'student' : student,})

########################
# Sign in (Log in)
########################

def sign_in(request):
    if not request.user.is_staff:
        logout(request)

    if request.GET['next'] and not request.user.is_anonymous:
        return redirect(request.GET['next'])

    form = AccountAuthForm(data = request.POST or None)
    template = 'account/sign_in.html'

    next_url = request.POST.get("next", "/")

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())

        return redirect(next_url)

    return render(request, template, {'form': form, 'nav_bar': True, 'next': next_url, })


def close(request):
    template = 'account/close.html'

    return render(request, template)

########################
# Sign up (Join)
########################

def sign_up(request):
    form = AccountCreateForm(data = request.POST or None)
    template = 'account/sign_up.html'

    if request.method == 'POST':
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            new_user = form.save()

            user = authenticate(username=username, password=password)
            user.is_staff = True
            user.save()

            login(request, user)

            return redirect("/")
        else:
            return render(request, template, {'form': form, 'nav_bar': True,})

    return render(request, template,  {'form': form,  'nav_bar': True,})

########################
# Sign out (Log out)
########################

@login_required
def sign_out(request):
    logout(request)

    return redirect('/')

@login_required
def sign_out_and_redirect(request, thread_unique_id=None):
    logout(request)

    referer = request.META.get('HTTP_REFERER')

    return redirect(referer)
