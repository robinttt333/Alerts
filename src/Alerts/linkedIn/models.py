from django.db import models
import markdown

# Create your models here.

class LinkedInPost(models.Model):
	image = models.TextField()
	body = models.TextField()
	created = models.TextField()

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.body[:50]

	def mark(self):
		self.body = markdown.markdown(self.body)