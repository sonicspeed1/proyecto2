
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),  
    path('api/', include('peinado.urls')),  
    path('api/', include('manicura_pedicura.urls')), 
    path('api/', include('cosmetico.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
