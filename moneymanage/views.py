from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request):
    return render(request, 'home.html')

def saving(request):
    return render(request, 'saving.html', {
        'new_sav_list': request.POST.get('description', ''),
    })

