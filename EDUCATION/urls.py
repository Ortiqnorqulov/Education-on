from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings
from creatoradmin import views as Creatortoradmin
from home import views

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectlanguage_admin', Creatortoradmin.selectlanguage_admin, name='selectlanguage_admin'),
    path('i18n/', include('django.conf.urls.i18n')),
]



urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('course/', include('course.urls')),
    path('creatoradmin/', include('creatoradmin.urls')),
    path('order/', include('order.urls')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
