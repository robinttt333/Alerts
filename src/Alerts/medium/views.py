from django.shortcuts import render
from .tasks import getUserNotifications, add, change_username
from .mediumBot import ScraperPersonal
# Create your views here.
def home(request):
	ScraperPersonal().getNotifications()
	return render(request, 'base.html', {})