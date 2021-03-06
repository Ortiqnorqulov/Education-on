# Generated by Django 4.0.3 on 2022-03-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_adversiting_description_adversiting_description_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCommentsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('New', 'Yangi'), ('Read', 'Read'), ('Closed', 'Yopilgan')], default='New', max_length=15)),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
