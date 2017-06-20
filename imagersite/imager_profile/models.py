"""Define imager profile class and it's methods."""


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class ImagerActiveManager(models.Manager):
    """Manager for the ImagerProfile Active API."""

    def get_queryset(self):
        """Return query of active users."""
        return super(ImagerActiveManager, self).get_queryset().filter(is_active=True)

@python_2_unicode_compatible
class Imager_Profile(models.Model):
    """A profile for users to our application."""
    user = models.OneToOneField(User)
    location = models.CharField(max_length=255)
    age = models.IntegerField()
    camera_type = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    active = ImagerActiveManager()

    STYLE_CHOICES = (
        ('MONO', 'Monochrome'),
        ('MACRO', 'Macro'),
        ('MICRO', 'Micro'),
        ('PORTRAIT', 'Portrait'),
        ('LANDSCAPE', 'Landscape')
    )

    photography_style = models.CharField(
        max_length=255,
        choices=STYLE_CHOICES,
        default='PORTRAIT',
    )

    SOCIAL_CHOICES = (
        ('PEASANT', 'Peasant'),
        ('KNIGHT', 'Knight'),
        ('MANATARMS', 'Man-at-Arms'),
        ('ROYALTY', 'Royalty'),
        ('BANDIT', 'Bandit'),
        ('BARBARIAN', 'Barbarian'),
        ('COW', 'Cow')
    )

    social_status = models.CharField(
        max_length=255,
        choices=SOCIAL_CHOICES,
        default='COW',
    )

    def is_active(self):
        """Return if profile is active."""
        return self.user.is_active

    def __str__(self):
        """Define a string representation of Imager_Profile."""
        return '(Username: {}, Location: {}, Age: {}, Camera Type: {}, Job: {}, Social Status: {}, Style: {}, URL: {})'\
            .format(
                self.user,
                self.location,
                self.age,
                self.camera_type,
                self.job,
                self.social_status,
                self.photography_style,
                self.url
                )


@receiver(post_save, sender=User)
def make_profile_for_new_user(sender, **kwargs):
    """Instantiate profile for new user."""
    if kwargs['created']:
        new_profile = Imager_Profile(
            user=kwargs['instance']
        )
        new_profile.save()
