"""Views for user profiles."""


from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from imager_profile.models import ImagerProfile


def profile_view(request):
    """View for the logged-in user's profile."""
    user = request.user
    albums = user.created_by.all()
    albums_pri = albums.filter(published='PRI').count()
    albums_pub = albums.filter(published='PUB').count()
    photos = user.created_by.all()
    photos_pri = photos.filter(published='PRI').count()
    photos_pub = photos.filter(published='PUB').count()
    return render(request, "imager_profile/profile.html", {
        "the_user": user,
        "albums": albums,
        "albums_pub": albums_pub,
        "albums_pri": albums_pri,
        "photos_pub": photos_pub,
        "photos_pri": photos_pri
    })


def other_profile_view(request, other_user):
    """View for any specified user's profile."""
    user = User.objects.all().filter(username=other_user).first()
    albums = user.created_by.all()
    albums_pub = albums.filter(published='PUB').count()
    photos = user.created_by.all()
    photos_pub = photos.filter(published='PUB').count()
    return render(request, "imager_profile/profile.html", {
        "the_user": user,
        "albums": albums,
        "albums_pub": albums_pub,
        "photos_pub": photos_pub
    })
