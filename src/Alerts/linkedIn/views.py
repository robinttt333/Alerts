from django.shortcuts import render

# Create your views here.
from .tasks import getUserNotifications
def home(request):
	getUserNotifications.delay()
	return render(request, 'base.html', {})