from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('profile/', include('uprofile.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
