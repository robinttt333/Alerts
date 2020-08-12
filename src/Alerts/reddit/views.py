from django.shortcuts import render

# Create your views here.
from .tasks import getHot
def home(request):
	getHot.delay()
	return render(request, "base.html", {})