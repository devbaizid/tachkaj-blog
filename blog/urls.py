
from django.contrib import admin
from django.urls import path,include
from api.views import *
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = "Tachkaj-blog Administration"
admin.site.index_title = "Tachkaj-blog Site Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
        path('api/', include('api.urls')),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)