from django.db import models
from ckeditor.fields import RichTextField

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtittle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider')
    crearted_time = models.DateTimeField(auto_now_add=True)
    button_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.headline

class team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y')
    created_time = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class contact_us(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class info(models.Model):
    heading = models.CharField(max_length=255,default='Company details')
    email = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    fb_link = models.CharField(max_length=955)
    insta_link = models.CharField(max_length=955)
    twitter_link = models.CharField(max_length=955)
    youtuber_link = models.CharField(max_length=955)
    street = models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class about_detail(models.Model):
    heading = models.CharField(max_length=255,default='summa')
    photo = models.ImageField(upload_to='media/about')
    description = RichTextField()

    def __str__(self):
        return self.heading