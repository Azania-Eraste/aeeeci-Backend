from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .viewset import CustomViewSet, ScoutViewSet

router = DefaultRouter()
router.register(r'customUser', CustomViewSet)
router.register(r'ScoutUser', ScoutViewSet)

urlpatterns = [
    path('api_User/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)