from rest_framework import serializers
from .models import Tag, Project, BlogPost, TeamMember, Roadmap

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'tags', 'published_date']

class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'summary', 'image', 'tags', 'published_date']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'photo', 'position_rank']

class RoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadmap
        fields = ['id', 'icon_name', 'title', 'description', 'published_date']