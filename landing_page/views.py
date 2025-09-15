from rest_framework import viewsets
from .models import Tag, Project, BlogPost, TeamMember, Roadmap
from .serializers import TagSerializer, ProjectSerializer, BlogPostSerializer, TeamMemberSerializer, RoadmapSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-published_date')
    serializer_class = ProjectSerializer

class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.all().order_by('-published_date')
    serializer_class = BlogPostSerializer

class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all().order_by('position_rank')
    serializer_class = TeamMemberSerializer

class RoadmapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Roadmap.objects.all().order_by('-published_date')
    serializer_class = RoadmapSerializer

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer