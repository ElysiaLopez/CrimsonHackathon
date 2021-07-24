from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('upload/', include('upload_section.urls', namespace='upload')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)