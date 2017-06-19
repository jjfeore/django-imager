"""Define imager profile class and it's methods."""


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.


class Imager_Profile(models.Model):
    """A profile for users to our application."""
    user = models.OneToOneField(User)
    location = models.CharField(max_length=255)
    age = models.IntegerField()
    camera_type = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    url = models.URLField(max_length=200)

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

    def __repr__(self):
        return self.user.username


@receiver(post_save, sender=User)
def make_profile_for_new_user(sender, **kwargs):
    """Instantiate profile for new user."""
    if kwargs['created']:
        new_profile = Imager_Profile(
            user=kwargs['instance']
        )
        new_profile.save()
