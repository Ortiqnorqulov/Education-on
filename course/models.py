from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from home.models import OurTeam


class Category(MPTTModel):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    parent = TreeForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='children',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/Category',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

class MPTTMeta:
    order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])



class Courses(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(OurTeam, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    lenguage = models.CharField(max_length=255, unique=True)
    duration = models.CharField(max_length=255, unique=True)
    level = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images/Course',
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png',])])
    old_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    sell_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CourseDetail(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=255, unique=True)
    number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.number