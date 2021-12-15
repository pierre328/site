
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import index
from blog import settings


urlpatterns = [
    path('toto/', admin.site.urls),
    path('blog/', include('posts.urls')),
    path('', index, name="index"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
