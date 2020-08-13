from django.db import models
import markdown

# Create your models here.

class LinkedInPost(models.Model):
	image = models.TextField()
	body = models.TextField()
	created = models.TextField()
	url = models.TextField()
	read = models.BooleanField(default = False)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.body[:50]

	def mark(self):
		self.body = markdown.markdown(self.body)

	def markWithoutP(self):
		p = '<p>'
		np = '</p>'
		md = markdown.markdown(self.body)
		if md.startswith(p) and md.endswith(np): 
		    md = md[len(p):-len(np)]
		self.body = md
		
	def makeUrl(self):
		return "https://linkedIn.com" + self.url