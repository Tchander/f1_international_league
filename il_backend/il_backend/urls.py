from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('api/v1/', include('international_league.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
