# Generated by Django 4.0.3 on 2022-03-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
