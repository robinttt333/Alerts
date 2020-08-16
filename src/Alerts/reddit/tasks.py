from __future__ import absolute_import, unicode_literals

from celery import shared_task
from reddit.models import RedditPost
from .redditBot import RedditBot

@shared_task
def getHot(subreddit = 'learnpython'):
	RedditBot().hot(subreddit)

@shared_task
def checkExistance(subreddit):
	exists = RedditBot().checkSubreddit(subreddit)
	if exists:
		getHot.delay(subreddit)
