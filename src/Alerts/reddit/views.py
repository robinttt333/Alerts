from django.shortcuts import render, reverse, redirect
import markdown
# Create your views here.
from .models import RedditPost
from .redditBot import RedditBot
from .tasks import checkExistance
from django.contrib import messages

subreddits = RedditPost.objects.values('subreddit').distinct()
subreddits = [ subreddit['subreddit'] for subreddit in subreddits ]

def home(request):
	qs = RedditPost.objects.all()
	for post in qs:
		post.mark()
	return render(request, "reddit/home.html", {'redditPosts' : qs, 'subreddits': subreddits})

def new(request):
	subreddit = request.POST.get('subreddit')
	checkExistance.delay(subreddit)
	messages.add_message(request, messages.SUCCESS, 'Your request is under process...If the subreddit exists, it shall be added')
	return redirect(reverse('reddit:home'))
