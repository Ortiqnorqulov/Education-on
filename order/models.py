from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from course.models import Courses
from creatoradmin.models import Client


class ShopCart(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.course

    @property
    def price(self):
        return (self.course.sell_price)


################################################################################################################
################################################################################################################
################################################################################################################


class Order(models.Model):
    STATUS = (
        ('Waiting', 'Kuting'),
        ('Accepted', 'Qabul qilingan'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    feedback = models.CharField(blank=True, max_length=20)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Waiting')
    ip = models.CharField(blank=True, max_length=25)
    adminnote = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class CourseCarts(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    user = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    country = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    title = models.CharField(blank=True, max_length=255)
    price = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/Blog',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])
    status = models.CharField(max_length=15, choices=STATUS, default='Waiting')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user