from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts"
    )
    Created_date = models.DateTimeField(default=timezone.now)
    Published_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.Title