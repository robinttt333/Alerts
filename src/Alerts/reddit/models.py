from django.db import models

# Create your models here.
class RedditPost(models.Model):
	title = models.TextField()
	body = models.TextField()
	comments = models.IntegerField()
	createdDate = models.DateField(auto_now_add = True)
	url = models.TextField()
	postId = models.CharField(max_length = 20)
	