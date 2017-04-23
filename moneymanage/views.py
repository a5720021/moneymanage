from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from moneymanage.models import Sav_list,Gold_price

def home(request):
    saving = Sav_list.objects.all()
    cur_money = 0
    in_money = 0
    out_money = 0
    for i in saving:
        if(i.sav_type == 'outcome'):
            cur_money -= i.amount
            out_money += i.amount
        else:
            cur_money += i.amount
            in_money += i.amount
    percent = float(cur_money) / (in_money+1) * 100
    return render(request, 'home.html',{'income' : in_money ,'outcome' : out_money ,'in_percent': float(percent),'current_money' : cur_money})

def saving(request):
    if request.method == 'POST':
        Sav_list.objects.create(description=request.POST['description'],amount=int(request.POST['value']),sav_type=request.POST['type'])
        return redirect('saving')

    items = Sav_list.objects.all()
    return render(request, 'saving.html',{'items': items})

def gold(request):
    gold_all = Gold_price.objects.all()
    return render(request, 'gold.html',{'goldall': gold_all})




