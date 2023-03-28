from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from gost.views import *
from home.views import *
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('documents/', include('gost.urls')),
    path('calc-capacitive-equipment/', include('capacitive_equipment.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
