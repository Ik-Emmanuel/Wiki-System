from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='authapp:signin')
def home(request):
    return render(request, 'encyclopedia/index.html')