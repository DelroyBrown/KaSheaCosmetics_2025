from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "KaSheaCosmetics_base"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("KaSheaCosmetics_home.urls")),
    path("catalog/", include(("catalog.urls", "catalog"), namespace="catalog")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
