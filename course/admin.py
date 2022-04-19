from django.contrib import admin
from course.models import Category, Courses, CourseDetail


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status', 'slug']
    list_filter = ['title']

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'old_price', 'sell_price', 'status', 'slug', 'level', 'lenguage', 'duration', 'link']
    list_filter = ['title']


class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ['number', 'description', 'link',]
    list_filter = ['number']

admin.site.register(Courses, CoursesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CourseDetail, CourseDetailAdmin)


