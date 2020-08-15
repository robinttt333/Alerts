from django.shortcuts import render, reverse, redirect
from django.conf import settings

def home(request):
	return redirect(reverse('reddit:home'))