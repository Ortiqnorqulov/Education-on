from django.contrib import admin
from home.models import ContactMessage, Informations, Slider, Blog, OurTeam, Aboutus, NewsLatter, Comment_blog, \
    FAQs, Adversiting, CourseCommentsMessage, CourseBuy


class InformationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city', 'address', 'phone', 'email', 'image', 'telegram', 'instagram',
                    'facebook', 'description', 'create_at', ]
    list_filter = ['status']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'creat_at', ]
    readonly_fields = ('name', 'email', 'phone', 'message', 'creat_at',)
    list_filter = ['status']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status' ]
    list_filter = ['title']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status' ]
    list_filter = ['title']

class AboutusAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'status' ]
    list_filter = ['title']


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'telegram', 'instagram',
                    'facebook', 'twitter', 'description',]
    list_filter = ['title']

class NewsLatterAdmin(admin.ModelAdmin):
    list_display = ['email', 'ip']
    list_filter = ['email']

class Comment_blogAdmin(admin.ModelAdmin):
    list_display = ['blog', 'name', 'email', 'comment', 'ip']
    list_filter = ['name']

class FAQsAdmin(admin.ModelAdmin):
    list_display = ['number', 'question', 'answer']
    list_filter = ['question']


class Adversitingdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']
    list_filter = ['title']


class CourseCommentsMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['name']

class CourseBuyAdmin(admin.ModelAdmin):
    list_display = ['username', 'title', 'email', 'phone']
    list_filter = ['username']

admin.site.register(Comment_blog, Comment_blogAdmin)
admin.site.register(Informations, InformationsAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(NewsLatter, NewsLatterAdmin)
admin.site.register(FAQs, FAQsAdmin)
admin.site.register(Adversiting, Adversitingdmin)
admin.site.register(CourseCommentsMessage, CourseCommentsMessageAdmin)
admin.site.register(CourseBuy, CourseBuyAdmin)




