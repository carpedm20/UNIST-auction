from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import Stuff, Deal

# Create your views here.
def index(request):
    template = "index.html"

    stuff = Stuff.objects.all()[0]

    if request.user.is_anonymous():
        thumb_url = None
    else:
        thumb_url = request.user.profile_image_url.replace("large", "normal")

    return render(request,
                  template,
                  {'stuff': stuff,
                   'thumb_url': thumb_url,})

def new_neal(request):
    referer = request.META.get('HTTP_REFERER') or reverse('core:index')

    if request.method == 'POST':
        reason = request.POST.get("reason", "")
        is_name_filter = request.POST.get("is_name_filter", False)
        price = request.POST.get("price", 0)

        print reason
        print is_name
        print price
        
        try:
            deal = Deal(stuff = Stuff.objects.all()[0],
                        account = request.user,
                        price = price,
                        reason = reason,
                        is_name_filter = is_name_filter)
            deal.save()
        except Exception as e:
            messages.error(request, e)

        return redirect(referer)

    return iedirect(referer)
