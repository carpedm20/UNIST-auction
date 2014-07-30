from django.shortcuts import render

from .models import Stuff, Deal

# Create your views here.
def index(request):
    template = "index.html"

    stuff = Stuff.objects.all()[0]
    thumb_url = request.user.profile_image_url.replace("large", "normal")

    return render(request,
                  template,
                  {'stuff': stuff,
                   'thumb_url': thumb_url,})
