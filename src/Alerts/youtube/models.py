from django.db import models

# Create your models here.
class YoutubeNotification(models.Model):
	videoLink = models.TextField()
	read = models.BooleanField()
	image = models.TextField()
	time = models.TextField()
	description = models.TextField()
	thumbnail = models.TextField()

	class Meta:
		ordering = ['-time','read','description']
		
	def __str__(self):
		return self.description

	def getVideoLink(self):
		return "https://youtube.com/" + self.videoLink