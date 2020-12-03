from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', include('userprofiles2.urls')),
    path('avatar/', include('avatar.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('analysis.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)