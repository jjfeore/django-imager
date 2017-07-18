"""Define the URLs for the profile routes."""


from django.conf.urls import url
from imager_profile.views import ProfileView, OtherProfileView, EditProfileView


app_name = 'imager_profile'

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name="profile"),
    url(r'^edit/$', EditProfileView.as_view(), name="edit_profile"),
    url(r'^(?P<other_user>[\w.@+]+)/$', OtherProfileView.as_view(), name="other_profile")
]
