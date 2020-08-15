from __future__ import absolute_import, unicode_literals

from celery import shared_task
from medium.models import MediumNotification
from .mediumBot import ScraperPersonal

@shared_task
def add(x, y):
    return x + y

@shared_task
def change_username(pk):
    Notification = MediumNotification.objects.get(pk = pk)
    Notification.username = 'default'
    Notification.save()

@shared_task
def getUserNotifications():
	notifications = ScraperPersonal().getNotifications()
	for notification in notifications:
		MediumNotification(**notification).save()
