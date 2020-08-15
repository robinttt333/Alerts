from __future__ import absolute_import, unicode_literals

from celery import shared_task
from reddit.models import RedditPost
from .redditBot import RedditBot

@shared_task
def getHot():
	RedditBot().hot()

@shared_task
def checkExistance(subreddit):
	exists = RedditBot().checkSubreddit(subreddit)