"""Define views for imagersite."""

from random import randint
from django.shortcuts import render
from imager_images.models import Photo

def home_view(request):
    """Home view callable, for the home page."""
    count = Photo.objects.count()
    r_num = randint(0, count - 1)
    image = Photo.objects.all()[r_num]
    context = {
        'page': ' | Home',
        'image': image
    }
    return render(request, 'imagersite/home.html', context=context)


def account_view(request):
    """User account profile view."""
    return render(request, 'imagersite/account.html')
