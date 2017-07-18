"""Views for user profiles."""


from django.contrib.auth.models import User
from django.urls import reverse_lazy
from imager_profile.models import ImagerProfile
from imager_images.models import Photo, Album
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from imager_profile.forms import UserProfileForm


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


class EditProfileView(LoginRequiredMixin, UpdateView):
    """View to edit your profile."""

    login_url = reverse_lazy("login")
    template_name = "imager_profile/edit_profile.html"
    model = ImagerProfile
    form_class = UserProfileForm


    def get_object(self):
        """Return specified user."""
        return ImagerProfile.objects.all().get(user=self.request.user)


    def form_valid(self, form):
        """Save on post."""
        self.object = form.save()
        self.object.user.first_name = form.cleaned_data['First Name']
        self.object.user.last_name = form.cleaned_data['Last Name']
        self.object.user.email = form.cleaned_data['Email']
        self.object.user.save()
        self.object.save()
        return redirect("/profile")
