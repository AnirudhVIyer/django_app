# Generated by Django 5.0.6 on 2024-07-03 18:15

import photo_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=photo_app.models.user_directory_path),
        ),
    ]
