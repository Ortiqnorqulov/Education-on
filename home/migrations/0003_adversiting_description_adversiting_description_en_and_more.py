# Generated by Django 4.0.3 on 2022-03-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_adversiting_aboutus_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adversiting',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='adversiting',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adversiting',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adversiting',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
