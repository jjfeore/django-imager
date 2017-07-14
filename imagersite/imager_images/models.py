from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

SHARING_CHOICES = (
    ('PRI', 'private'),
    ('SHA', 'shared'),
    ('PUB', 'public')
)


class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_published = models.DateField(default=datetime.date.today)
    date_modified = models.DateField(auto_now=True)
    published = models.CharField(
        max_length=3,
        choices=SHARING_CHOICES,
        default='PRI',
    )
    image = models.ImageField(upload_to='photos', null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')

    def __repr__(self):
        return "<Photo: {}>".format(self.title)

    def __str__(self):
        """Display title."""
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_published = models.DateField(default=datetime.date.today)
    date_modified = models.DateField(auto_now=True)
    published = models.CharField(
        max_length=3,
        choices=SHARING_CHOICES,
        default='PRI',
    )
    photoset = models.ManyToManyField(Photo, related_name='in_album')
    cover = models.ForeignKey(Photo, related_name="covers", blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')

    def __repr__(self):
        return "<Album: {}>".format(self.title)

    def __str__(self):
        """Display title."""
        return self.title
