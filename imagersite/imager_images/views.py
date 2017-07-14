"""Views for photos, albums, and library."""


from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from imager_images.models import Album, Photo


class LibraryView(LoginRequiredMixin, TemplateView):
    """View for the library."""

    template_name = "imager_images/library.html"
    login_url = reverse_lazy("login")

    def get_context_data(self):
        """Return all the user's albums and photos."""
        user = self.request.user
        album_list = user.albums.all()
        photo_list = user.photos.all()
        return {"albums": album_list, "photos": photo_list}


class PhotosView(ListView):
    """View all the photos."""

    template_name = "imager_images/photos.html"
    model = Photo
    context_object_name = "photos"

    def get_queryset(self):
        """Return user's published photos."""
        return self.request.user.photos.all().filter(published='PUB')


class AlbumsView(ListView):
    """View all albums."""

    template_name = "imager_images/albums.html"
    model = Album
    context_object_name = "albums"

    def get_queryset(self):
        """Return user's published albums."""
        return self.request.user.albums.all().filter(published='PUB')


class AddPhotoView(LoginRequiredMixin, CreateView):
    """Add a Photo to the user."""

    login_url = reverse_lazy("login")
    template_name = "imager_images/add_photo.html"
    model = Photo
    fields = [
        "title", "description", "published", "date_published", "image"
    ]

    def form_valid(self, form):
        """Force the form to use the current user as the uploader."""
        form.instance.uploaded_by = self.request.user
        photo = form.save()
        photo.uploaded_by = self.request.user
        photo.save()
        return redirect("/images/library/")


class AddAlbumView(LoginRequiredMixin, CreateView):
    """Add an Album to the user."""

    login_url = reverse_lazy("login")
    template_name = "imager_images/add_album.html"
    model = Album
    fields = [
        "title", "description", "cover", "published", "date_published", "photoset"
    ]

    def form_valid(self, form):
        """Force the form to use the current user as the creator."""
        form.instance.created_by = self.request.user
        album = form.save()
        album.created_by = self.request.user
        album.save()
        return redirect("/images/library/")
