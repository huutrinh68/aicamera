from django.shortcuts import render
from django.contrib.auth.models import User

def new_user(request):
	users = User.objects.all()

	return render(request, 'new_user.html', {'users':users})