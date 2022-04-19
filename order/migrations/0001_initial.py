# Generated by Django 4.0.3 on 2022-03-20 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creatoradmin', '0001_initial'),
        ('course', '0005_alter_courses_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.courses')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='creatoradmin.client')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(editable=False, max_length=5)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('feedback', models.CharField(blank=True, max_length=20)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.CharField(choices=[('Waiting', 'Kuting'), ('Accepted', 'Qabul qilingan')], default='Waiting', max_length=15)),
                ('ip', models.CharField(blank=True, max_length=25)),
                ('adminnote', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]