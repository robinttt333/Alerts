from django.shortcuts import render

# Create your views here.
from .tasks import getUserNotifications
from .models import LinkedInPost
def home(request):
	qs = LinkedInPost.objects.all()
	for post in qs:
		post.mark()
	return render(request, 'home.html', {'linkedInPosts': qs})