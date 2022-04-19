from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coursesall/', views.coursesall, name='coursesall'),
    path('blog/', views.blog, name='blog'),
    path('coursebuy/', views.coursebuy, name='coursebuy'),
    path('contact/', views.contact, name='contact'),
    path('course_detail/<int:id>/<slug:slug>', views.course_detail, name='course_detail'),
    path('faq/', views.faq, name='faq'),
    path('newsLatter/', views.newsLatter, name='newsLatter'),
    path('eror404/', views.eror404, name='eror404'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('category_course/<int:id>', views.category_course, name='category_course'),
    path('search/', views.search, name='search'),
]