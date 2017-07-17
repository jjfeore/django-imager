"""Views for photos, albums, and library."""


from django.http import HttpResponseForbidden
from django.shortcuts import render
from imager_images.models import Album, Photo
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User
from django.conf import settings


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
