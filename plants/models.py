from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# from taggit.managers import TaggableManager

# Create your models here.
class Plant(models.model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    content = models.TextField()
    preferences = models.CharField(max_length=20)
    allergy = models.CharField(max_length=20)
    flowering = models.CharField(max_length=20)
    season = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    watering = models.CharField(max_length=20)
    sunlight = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    temperature = models.CharField(max_length=20)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_plants')
    def plant_images_path(instance, filename):
        return f'products/{instance.title}/{filename}'
    image = ProcessedImageField(
        upload_to=plant_images_path, 
        processors=[ResizeToFit(800, 800)], 
        format='JPEG', 
        options={'quality': 100}
    )