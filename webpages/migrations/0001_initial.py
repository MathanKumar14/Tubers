# Generated by Django 3.1.5 on 2021-01-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('subtittle', models.CharField(max_length=255)),
                ('button_text', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/slider')),
                ('crearted_time', models.DateTimeField(auto_now_add=True)),
                ('button_link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('fb_link', models.CharField(max_length=255)),
                ('insta_link', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('youtube_link', models.CharField(max_length=255)),
            ],
        ),
    ]
