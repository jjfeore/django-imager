"""Define views for imagersite."""

from random import randrange
from django.shortcuts import render
from imager_images.models import Photo


def home_view(request):
    """Home view callable, for the home page."""
    try:
        count = Photo.objects.count()
        r_num = randrange(0, count)
        image = Photo.objects.all()[r_num]
    except ValueError:
        image = None
    context = {
        'page': ' | Home',
        'image': image
    }
    return render(request, 'imagersite/home.html', context=context)
