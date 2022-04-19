# Generated by Django 4.0.3 on 2022-03-18 22:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_adversiting_description_adversiting_description_en_and_more'),
        ('course', '0003_course_description_en_course_description_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('title_en', models.CharField(max_length=255, null=True, unique=True)),
                ('title_ru', models.CharField(max_length=255, null=True, unique=True)),
                ('title_uz', models.CharField(max_length=255, null=True, unique=True)),
                ('lenguage', models.CharField(max_length=255, unique=True)),
                ('lenguage_en', models.CharField(max_length=255, null=True, unique=True)),
                ('lenguage_ru', models.CharField(max_length=255, null=True, unique=True)),
                ('lenguage_uz', models.CharField(max_length=255, null=True, unique=True)),
                ('duration', models.CharField(max_length=255, unique=True)),
                ('level', models.CharField(max_length=255, unique=True)),
                ('level_en', models.CharField(max_length=255, null=True, unique=True)),
                ('level_ru', models.CharField(max_length=255, null=True, unique=True)),
                ('level_uz', models.CharField(max_length=255, null=True, unique=True)),
                ('link', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/Product', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.CharField(choices=[('True', 'Mavjud'), ('False', 'Mavjud Emas')], max_length=15)),
                ('slug', models.SlugField(unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ourteam')),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
