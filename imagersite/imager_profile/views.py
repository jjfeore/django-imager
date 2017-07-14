"""Views for user profiles."""


from django.contrib.auth.models import User
from django.urls import reverse_lazy
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, DetailView):
    """View for the logged-in user's profile."""

    template_name = "imager_profile/profile.html"
    model = ImagerProfile
    login_url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        """Get object from request instead of pk."""
        user = request.user
        albums = Album.objects.all().filter(created_by=user)
        albums_pri = albums.filter(published='PRI').count()
        albums_pub = albums.filter(published='PUB').count()
        photos = Photo.objects.all().filter(uploaded_by=user)
        photos_pri = photos.filter(published='PRI').count()
        photos_pub = photos.filter(published='PUB').count()
        return self.render_to_response({
            "the_user": user,
            "albums": albums,
            "albums_pub": albums_pub,
            "albums_pri": albums_pri,
            "photos_pub": photos_pub,
            "photos_pri": photos_pri
        })


class OtherProfileView(DetailView):
    """View for any specified user's profile."""

    template_name = "imager_profile/profile.html"
    model = ImagerProfile

    def get(self, request, *args, **kwargs):
        """Get object from request instead of pk."""
        user = User.objects.all().filter(username=self.kwargs['other_user']).first()
        albums = Album.objects.all().filter(created_by=user)
        albums_pub = albums.filter(published='PUB').count()
        photos = Photo.objects.all().filter(uploaded_by=user)
        photos_pub = photos.filter(published='PUB').count()
        return self.render_to_response({
            "the_user": user,
            "albums": albums,
            "albums_pub": albums_pub,
            "photos_pub": photos_pub
        })
