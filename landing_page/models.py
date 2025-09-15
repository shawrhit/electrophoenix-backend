from datetime import timezone

from django.db import models
from django.template.defaulttags import now


# Model for reusable tags (e.g., "Robotics", "AI/ML")
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Model for the Project Showcase section
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    tags = models.ManyToManyField(Tag)
    published_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

# Model for the Latest Blogs section
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="A short summary for the landing page card.")
    image = models.ImageField(upload_to='blog_images/')
    tags = models.ManyToManyField(Tag)
    published_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

# Model for the Our Team section
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    position_rank = models.PositiveIntegerField(default=99,
                                                help_text="Lower number = higher seniority (e.g., 1 for President)")
    def __str__(self):
        return self.name

# Model for the Roadmaps section
class Roadmap(models.Model):
    icon_name = models.CharField(max_length=50, help_text="e.g., '🤖' or 'circuit-board'")
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title