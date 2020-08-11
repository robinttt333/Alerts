from django.db import models

# Create your models here.
class MediumNotification(models.Model):
	ACTIVITY_CHOICES = (
		('clapped', 'clapped for'), 
		('followed', 'started following'),
		('highlighted', 'highlighted for')
	) 
	username = models.CharField(max_length = 50)
	activityType = models.CharField(max_length = 30, choices = ACTIVITY_CHOICES)
	content = models.TextField()
