from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .youtubeBot import youtubeScraper
from .models import YoutubeNotification

@shared_task
def getUserNotifications():
	notifications  = youtubeScraper().getNotifications()
	
	for notification in notifications:
		YoutubeNotification(**notification).save()
	

