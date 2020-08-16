from django.shortcuts import render, reverse, redirect
import markdown
# Create your views here.
from .models import RedditPost
from .redditBot import RedditBot
from .tasks import checkExistance
from django.contrib import messages

LIMIT = 5
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
	if RedditPost.objects.values('subreddit').distinct().count() == LIMIT:
		return redirect(reverse('reddit:remove'))

	curr = request.POST.get('current').strip()
	checkExistance.delay(subreddit)
	messages.add_message(request, messages.SUCCESS, r'Your request is under process...If the subreddit <b>%s</b> exists, it shall be added'%subreddit)
	return redirect(reverse('reddit:home', kwargs={'subreddit': curr}))


def remove(request):
	if request.POST:
		subreddits = request.POST.getlist('subreddit')
		if len(subreddits) is 0:
			messages.add_message(request, messages.WARNING, 'Please select atleast one subreddit')
		else :
			for subreddit in subreddits:
				RedditPost.objects.filter(subreddit = subreddit).delete()
			messages.add_message(request, messages.SUCCESS, 'Successfully removed the selected subreddits')
			return redirect(reverse('reddit:home'))

	subreddits = RedditPost.objects.values('subreddit').distinct()
	subreddits = [ subreddit['subreddit'] for subreddit in subreddits ]
	if len(subreddits) is not LIMIT:
		messages.add_message(request, messages.ERROR,'Invalid path chosen')
		return redirect(reverse('reddit:home'))
	messages.add_message(request, messages.WARNING, 'Unfortunately you cannot add any more subreddits')
	return render(request, "reddit/removeSubreddit.html", {'subreddits' : subreddits})
