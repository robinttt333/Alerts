from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .linkedInBot import linkedInScraper
from .models import LinkedInPost
@shared_task
def getUserNotifications():
	notifications  = linkedInScraper().getNotifications()
	for notification in notifications:
		qs = LinkedInPost.objects.filter(url = notification['url'])
		if not qs:
			LinkedInPost(**notification).save()

