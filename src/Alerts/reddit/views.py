from django.shortcuts import render
import markdown
# Create your views here.
from .models import RedditPost
def home(request):
	qs = RedditPost.objects.all()
	for post in qs:
		post.mark()
	return render(request, "redditPosts.html", {'redditPosts' : qs})