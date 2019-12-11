from django.shortcuts import render
from app import models, scrapper
# Create your views here.


def mainHome(request):
    return render(request, 'base.html')

def searchView(request):
    q = request.POST.get('q')
    data = scrapper.fetchItems(q) if q else None
    
    ctx = {'q':q, 'data': data}
    return render(request, 'base.html', ctx)