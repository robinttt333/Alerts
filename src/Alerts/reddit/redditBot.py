import praw
from django.conf import settings
config = settings.CONFIG

class RedditBot:
    def __init__(self):
        self.clientId = config.get('reddit').get('clientId')
        self.clientSecret = config.get('reddit').get('clientSecret')
        self.userAgent = config.get('reddit').get('userAgent')
        self.crawler = praw.Reddit(client_id = self.clientId, client_secret = self.clientSecret, user_agent = self.userAgent)
    
    def crawl(self, subreddit):
        pass
    
    def hot(self, subreddit = "learnpython", limit=10):
        for submission in self.crawler.subreddit(subreddit).hot(limit=limit):
            print(submission.title)
        