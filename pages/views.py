from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage_view(request):
    return render(request, 'home.html') #takes in template name and context