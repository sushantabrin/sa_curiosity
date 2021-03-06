
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from curiosity import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('', include('curiosity.urls')),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
