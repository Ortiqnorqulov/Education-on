from django.db import models
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.core.validators import FileExtensionValidator


class Informations(models.Model):
    STATUS =(
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=300)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True,upload_to='images/Info',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Informations)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Informations.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)



class ContactMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', 'Read'),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    phone = models.TextField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Slider',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Slider)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Slider.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


class Blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/Blog',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Blog)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Blog.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


class Comment_blog(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=True)
    email = models.CharField(max_length=55, blank=True)
    comment = models.TextField(max_length=255,blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class OurTeam(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/Blog',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    description = models.TextField(blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    status = models.CharField(max_length=15, choices=STATUS)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Blog)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Blog.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


class Aboutus(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Aboutus',
    validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

@receiver(pre_save, sender=Aboutus)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Aboutus.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)


class NewsLatter(models.Model):
    email = models.CharField(max_length=255)
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class FAQs(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    number = models.CharField(max_length=9)
    question  = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    def __str__(self):
        return self.question


class Adversiting(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Slider',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CourseCommentsMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', 'Read'),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CourseBuy(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    username = models.CharField(blank=True, max_length=255)
    title = models.CharField(blank=True, max_length=255)
    email= models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username