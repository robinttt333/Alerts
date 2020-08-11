from django.shortcuts import render
from .tasks import getUserNotifications
# Create your views here.
def home(request):
	getUserNotifications().delay()
	return render(request, 'base.html', {})