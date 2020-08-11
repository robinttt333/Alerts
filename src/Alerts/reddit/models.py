from django.db import models

# Create your models here.
class RedditPost(models.Model):
	title = models.TextField()
	