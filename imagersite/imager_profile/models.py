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
class ImagerProfile(models.Model):
    """A profile for users to our application."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, default='Seattle, WA')
    age = models.IntegerField(default='25')
    camera_type = models.CharField(max_length=255, default='Polaroid')
    job = models.CharField(max_length=255, default='Developer')
    url = models.URLField(max_length=200, default='github.com/jjfeore')
    objects = models.Manager()
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

    @property
    def is_active(self):
        """Return if profile is active."""
        return self.user.is_active

    def __str__(self):
        """Define a string representation of Imager_Profile."""
        return '(Username: {}, Location: {}, Age: {}, Camera Type: {}, \
        Job: {}, Social Status: {}, Style: {}, URL: {})'\
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
        new_profile = ImagerProfile(
            user=kwargs['instance']
        )
        new_profile.save()
