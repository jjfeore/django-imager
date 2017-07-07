"""Define the URLs for the profile routes."""


from django.conf.urls import url
from . import views


app_name = 'imager_profile'

urlpatterns = [
    url(r'^$', views.profile_view, name="profile"),
    url(r'^profile/(?P<other_user>[.@+-%\w]+)/$', views.other_profile_view, name="other_profile")
]
