from django.shortcuts import render
from .tasks import getUserNotifications, add, change_username
from .mediumBot import ScraperPersonal
from .models import MediumNotification
# Create your views here.
def home(request):
	qs = MediumNotification.objects.all()
	return render(request, 'medium/home.html', {'mediumNotifications': qs})