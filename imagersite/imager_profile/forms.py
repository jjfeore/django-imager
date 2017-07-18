"""Form to edit profile."""

from django import forms
from imager_profile.models import ImagerProfile


class UserProfileForm(forms.ModelForm):
    """Form to edit profile.

    Shamelessly stolen from Ted's repo. Which was stolen was from Claire. Thanks Claire!
    """

    def __init__(self, *args, **kwargs):
        """Populate form fields with existing user info."""
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields["First Name"] = forms.CharField(
            initial=self.instance.user.first_name)
        self.fields["Last Name"] = forms.CharField(
            initial=self.instance.user.last_name)
        self.fields["Email"] = forms.EmailField(
            initial=self.instance.user.email)
        del self.fields["user"]

    class Meta:
        """Specify model and fields to exclude."""

        model = ImagerProfile
        exclude = []
