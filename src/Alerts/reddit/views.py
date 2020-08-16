from django.shortcuts import render, reverse, redirect
import markdown
# Create your views here.
from .models import RedditPost
from .redditBot import RedditBot
from .tasks import checkExistance
from django.contrib import messages


def home(request, subreddit = None):
	if subreddit is None:
		return redirect(reverse('reddit:home', kwargs={'subreddit':"learnpython"}))
	subreddits = RedditPost.objects.values('subreddit').distinct()
	subreddits = [ subreddit['subreddit'] for subreddit in subreddits ]
	
	qs = RedditPost.objects.filter(subreddit = subreddit)
	for post in qs:
		post.mark()
	return render(request, "reddit/home.html", {'redditPosts' : qs, 'subreddits': subreddits, 'subreddit' : subreddit})

def new(request):
	subreddit = request.POST.get('subreddit')
	curr = request.POST.get('current').strip()
	checkExistance.delay(subreddit)
	messages.add_message(request, messages.SUCCESS, r'Your request is under process...If the subreddit <b>%s</b> exists, it shall be added'%subreddit)
	return redirect(reverse('reddit:home', kwargs={'subreddit': curr}))
