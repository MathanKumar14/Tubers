from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Ytuber(models.Model):

    crew_choices = [
        ['solo','solo'],
        ['small','small'],
        ['large','large']
    ]

    camera_choices = [
        ['cannon','cannon'],
        ['nikon','nikon'],
        ['sony','sony'],
        ['panasonic','panasonic'],
        ['nokia','nokia']
    ]

    category_choices = [
        ['coding','coding'],
        ['comedy','comedy'],
        ['short_film','short-film'],
        ['mobile_review','mobile_review'],
        ['others','others']
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y/%m')
    age = models.IntegerField()
    description = RichTextField()
    video_url = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now())