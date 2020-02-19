from django.shortcuts import render
from django.http import HttpResponse
import random 

def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	# characters = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()_+'))

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))

	# the 12 is default on the line below
	length = int(request.GET.get('length', 12)); 

	thepassword = ''

	for x in range(length):
		thepassword += random.choice(characters)


	return render(request, 'generator/password.html', {'password':thepassword})

# Create your views here.

def about(request):
	return render(request, 'generator/about.html')
