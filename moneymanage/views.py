from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def saving(request):
    return render(request, 'saving.html')
