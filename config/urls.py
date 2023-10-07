from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter


from amigosjvll.views import EspecieViewSet
from amigosjvll.views import CorViewSet
from amigosjvll.views import AnimalViewSet
from amigosjvll.views import RacaViewSet


router = DefaultRouter()
router.register(r"especies", EspecieViewSet)
router.register(r"animais", AnimalViewSet)
router.register(r"racas", RacaViewSet)
router.register(r"cores", CorViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)