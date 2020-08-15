from django.shortcuts import render
from .tasks import getUserNotifications
from .models import YoutubeNotification
# Create your views here.
def home(request):
	# getUserNotifications.delay()
	qs = YoutubeNotification.objects.all()
	youtubeNotifications = []
	for youtubeNotification in qs:
		youtubeNotifications.append(youtubeNotification)
		youtubeNotification.read = True
		youtubeNotification.save()
		
	return render(request, "youtube/home.html", {"youtubeNotifications": youtubeNotifications})