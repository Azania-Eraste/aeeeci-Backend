from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .viewset import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api_Event/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)