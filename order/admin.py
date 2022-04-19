from django.contrib import admin
from order.models import CourseCarts


class CourseCartsAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone', 'email', 'country', 'city', 'title', 'price', 'image',]
    list_filter = ['name']

admin.site.register(CourseCarts, CourseCartsAdmin)
