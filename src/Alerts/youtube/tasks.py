from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .youtubeBot import youtubeScraper

@shared_task
def getUserNotifications():
	notifications  = youtubeScraper().getNotifications()
	

