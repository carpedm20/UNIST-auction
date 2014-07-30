from django.shortcuts import render

from .models import Stuff, Deal

# Create your views here.
def index(request):
    template = "index.html"

    stuff = Stuff.objects.all()[0]

    return render(request,
                  template,
                  {'stuff': stuff,})
