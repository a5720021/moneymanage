from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from moneymanage.models import Sav_list

def home(request):
    return render(request, 'home.html')

def saving(request):
    if request.method == 'POST':
        Sav_list.objects.create(description=request.POST['description'],amount=int(request.POST['value']),sav_type=request.POST['type'])
        return redirect('saving')

    items = Sav_list.objects.all()
    return render(request, 'saving.html',{'items': items})



