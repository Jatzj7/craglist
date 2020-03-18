from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    context = {
        'serach': search
    }
    return render(request, 'main_app/new_search.html', context)
