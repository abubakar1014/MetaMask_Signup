from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'user/home.html')

def auth(request):
    return render(request, 'user/metaauth.html')