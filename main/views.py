from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Home',
        'content': 'Главная страница сайта - HOME'
    }

    return render(request, 'main/index.html', context)

def faq(request):
    return HttpResponse('FAQ page')
