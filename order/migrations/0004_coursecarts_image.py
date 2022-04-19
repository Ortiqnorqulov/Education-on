# Generated by Django 4.0.3 on 2022-03-21 20:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_coursecarts_city_coursecarts_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecarts',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/Blog', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]