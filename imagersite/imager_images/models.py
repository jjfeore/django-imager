from django.db import models
import uuid
import datetime

# Create your models here.

SHARING_CHOICES = (
    ('PRI', 'private'),
    ('SHA', 'shared'),
    ('PUB', 'public')
)

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_uploaded = models.DateField(auto_now_add=True)
    date_published = models.DateField(auto_now=True)
    date_modified = models.DateField(default=datetime.date.today)
    img_id = models.UUIDField(default=uuid.uuid4, editable=False)
    published = models.CharField(
        max_length=3,
        choices=SHARING_CHOICES,
        default='PRI',
    )
    image = models.ImageField(upload_to='photos', null=True)
    uploaded_by = models.ForeignKey('imager_profile.ImagerProfile', on_delete=models.CASCADE, related_name='photos')

    def __repr__(self):
        return "<Photo: {}>".format(self.title)


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_published = models.DateField(auto_now=True)
    date_modified = models.DateField(default=datetime.date.today)
    img_id = models.UUIDField(default=uuid.uuid4, editable=False)
    published = models.CharField(
        max_length=3,
        choices=SHARING_CHOICES,
        default='private',
    )
    photoset = models.ManyToManyField(Photo, related_name='in_album')
    cover = models.ImageField(upload_to='photos', null=True)
    created_by = models.ForeignKey('imager_profile.ImagerProfile', on_delete=models.CASCADE, related_name='albums')

    def __repr__(self):
        return "<Album: {}>".format(self.title)
