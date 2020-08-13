from django.shortcuts import render

# Create your views here.
from .tasks import getHot
from .models import RedditPost
def home(request):
	qs = RedditPost.objects.all()
	return render(request, "redditPosts.html", {'redditPosts' : qs})