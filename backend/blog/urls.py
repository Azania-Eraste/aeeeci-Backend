from django.urls import path,include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from .serializers import ArticleDetailAPIView
from blog.viewsets import ArticleViewSet, CategorieViewSet, TagViewSet, CommentaireViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategorieViewSet)
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'tag', TagViewSet)
router.register(r'commentaire', CommentaireViewSet, basename='commentaire')


app_name="blog"

urlpatterns = [
    path('api/articles/<slug:slug>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('api_Blog/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
