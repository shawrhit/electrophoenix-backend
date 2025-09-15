from django.contrib import admin
from .models import Tag, Project, BlogPost, TeamMember, Roadmap

# Register your models here so they appear in the admin panel.
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(TeamMember)
admin.site.register(Roadmap)
