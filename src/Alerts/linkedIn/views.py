from django.shortcuts import render

# Create your views here.
from .tasks import getUserNotifications
from .models import LinkedInPost
def home(request):
	getUserNotifications.delay()
	qs = LinkedInPost.objects.all()
	posts = []
	for post in qs:
		post.markWithoutP()
		posts.append(post)
		post.read = True
		post.save()
	return render(request, 'home.html', {'linkedInPosts': posts})