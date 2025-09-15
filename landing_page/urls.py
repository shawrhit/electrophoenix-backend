from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, ProjectViewSet, BlogPostViewSet, TeamMemberViewSet, RoadmapViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'roadmaps', RoadmapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
