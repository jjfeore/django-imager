"""Views for user profiles."""


from django.shortcuts import render
from django.contrib.auth.models import User
from django.conf import settings
from imager_profile.models import ImagerProfile


def profile_view(request):
    """View for the logged-in user's profile."""
    user = request.user
    albums = user.created_by.all()
    return render(request, "imager_profile/profile.html", {"the_user": user, "albums": albums})


def other_profile_view(request, other_user):
    """View for any specified user's profile."""
    user = User.objects.all().filter(username=other_user).first()
    albums = user.created_by.all()
    return render(request, "imager_profile/profile.html", {"the_user": user, "albums": albums})
