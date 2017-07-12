"""Define views for imagersite."""

from random import randrange
from imager_images.models import Photo
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home view callable, for the home page."""

    template_name = "imagersite/home.html"

    def get_context_data(self):
        """Get necessary data for Home view."""
        try:
            count = Photo.objects.count()
            r_num = randrange(0, count)
            image = Photo.objects.all()[r_num]
        except ValueError:
            image = None
        return {
            'page': ' | Home',
            'image': image
        }
