from django.shortcuts import render,redirect,render_to_response
from django.http import HttpRequest,HttpResponse
from moneymanage.models import Sav_list,Gold_price,Stock,Bank
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

def home(request,user_name):
    saving = Sav_list.objects.filter(owner=user_name)
    cur_gold = Gold_price.objects.order_by('-add_time')
    interest_stock = Stock.objects.order_by('-change')
    top_bank_sav = Bank.objects.order_by('-saving')
    top_bank_fixed = Bank.objects.order_by('-fixed_max')
    cur_money = 0
    in_money = 0
    out_money = 0
    for i in saving:
        if(i.sav_type == 'expense'):
            cur_money -= i.amount
            out_money += i.amount
        else:
            cur_money += i.amount
            in_money += i.amount
    percent = "{0:.2f}".format(float(cur_money) / (in_money+1) * 100)
    return render(request, 'home.html',{'income' : in_money ,'outcome' : out_money ,'in_percent': float(percent),'current_money' : cur_money,'gold' : cur_gold ,'stock' : interest_stock ,'sav' : top_bank_sav,'fixed' : top_bank_fixed,'user':user_name})

def saving(request,user_name):
    if request.method == 'POST':
        Sav_list.objects.create(description=request.POST['description'],amount=int(request.POST['value']),sav_type=request.POST['type'],owner=user_name)
        return redirect('/%s/saving' %(user_name))

    items = Sav_list.objects.filter(owner=user_name)
    return render(request, 'saving.html',{'items': items,'user' : user_name})

def gold(request,user_name):
    gold_all = Gold_price.objects.order_by('-add_time')
    return render(request, 'gold.html',{'goldall': gold_all,'user' : user_name})

def stock(request,user_name):
    stock = Stock.objects.all()
    return render(request, 'stock.html',{'stockall': stock,'user' : user_name})

def bank(request,user_name):
    bank = Bank.objects.all()
    return render(request, 'bank.html',{'bankall': bank,'user' : user_name})

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('/%s/' %(username))

    else:
        return HttpResponse("Error invaid login.")

def logout_view(request,user_name):
    logout(request)
    return redirect('/')

def index(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register2(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    return render(request, 'register.html')

def delete(request,user_name):
    delid = request.POST['delid']
    Sav_list.objects.filter(id=delid).delete()
    return redirect('/%s/saving' %(user_name))