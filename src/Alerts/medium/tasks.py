from __future__ import absolute_import, unicode_literals

from celery import shared_task
from medium.models import MediumNotification
from .mediumBot import ScraperPersonal

@shared_task
def getUserNotifications():
	notifications = ScraperPersonal().getNotifications()
	for notification in notifications:
		qs = MediumNotification.objects.filter(description = notification['description'])
		if not qs:
			MediumNotification(**notification).save()
