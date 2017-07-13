"""Views for photos, albums, and library."""


from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from imager_images.models import Album, Photo


def library_view(request):
    """Display the user's library of albums/photos."""
    if request.user.is_authenticated():
        user = request.user
        album_list = user.albums.all()
        photo_list = user.photos.all()
        return render(
            request,
            "imager_images/library.html",
            {
                "albums": album_list,
                "photos": photo_list
            }
        )
    return HttpResponseForbidden()


def photos_view(request):
    """Display all the user's photos."""
    if request.user.is_authenticated():
        photos = Photo.objects.all().filter(uploaded_by=request.user)
        return render(request, "imager_images/photos.html", {"photos": photos})
    return HttpResponseForbidden()


def photo_detail_view(request, pk):
    """Display detail view for a single photo."""
    if request.user.is_authenticated():
        photo = Photo.objects.get(pk=pk)
        return render(request, "imager_images/photo_detail.html", {"photo": photo})


def albums_view(request):
    """Display all the user's albums."""
    if request.user.is_authenticated():
        albums = Album.objects.all().filter(created_by=request.user)
        return render(request, "imager_images/albums.html", {"albums": albums})


def album_detail_view(request, pk):
    """Display detail view for a single album."""
    if request.user.is_authenticated():
        album = Album.objects.get(pk=pk)
        photos = album.in_album.all()
        return render(request, "imager_images/album_detail.html", {"photos": photos, "album": album})


class LibraryView(LoginRequiredMixin, TemplateView):
    """View for the library."""

    template_name = "imager_images/library.html"
    login_url = reverse_lazy("login")

    def get_context_data(self):
        user = self.request.user
        album_list = user.albums.all()
        photo_list = user.photos.all()
        return {"albums": album_list, "photos": photo_list}


class PhotosView(ListView):
    """View all the photos."""

    template_name = "imager_images/photos.html"

    def get_context_data(self):
        user = self.request.user
        photo_list = user.photos.all().filter(published='PUB')
        return {"photos": photo_list}


class AlbumsView(ListView):
    """View all albums."""

    template_name = "imager_images/albums.html"
    model = Album
    context_object_name = "albums"

    def get_queryset(self):
        """Modify get_queryset to return list of published albums for specific user."""
        return Album.published_albums.filter(owner=self.request.user)


class AddPhotoView(LoginRequiredMixin, CreateView):
    """Add a Photo to the user."""

    login_url = reverse_lazy("login")
    template_name = "imager_images/add_photo.html"
    model = Photo
    fields = [
        "title", "description", "published", "date_published", "image"
    ]

    def form_valid(self, form):
        """Force the form to use the current user as the author."""
        form.instance.author = self.request.user
        photo = form.save()
        photo.author = self.request.user
        photo.save()
        return redirect("/images/library/")


class AddAlbumView(LoginRequiredMixin, CreateView):
    """Add an Album to the user."""

    login_url = reverse_lazy("login")
    template_name = "imager_images/add_album.html"
    model = Album
    fields = [
        "title", "description", "album_cover", "published", "date_published", "pictures"
    ]

    def form_valid(self, form):
        """Force the form to use the current user as the author."""
        form.instance.owner = self.request.user
        album = form.save()
        album.owner = self.request.user
        album.save()
        return redirect("/images/library/")
