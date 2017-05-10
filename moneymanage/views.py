from django.shortcuts import render,redirect,render_to_response
from django.http import HttpRequest,HttpResponse
from moneymanage.models import Sav_list,Gold_price,Stock,Bank
from django.contrib.auth import authenticate, login

def home(request,user_name):
    saving = Sav_list.objects.filter(owner=user_name)
    cur_gold = Gold_price.objects.all().order_by('-add_time').first()
    interest_stock = Stock.objects.all().order_by('-change').first()
    top_bank_sav = Bank.objects.all().order_by('-saving').first()
    top_bank_fixed = Bank.objects.all().order_by('-fixed_max').first()
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
    percent = "{0:.2f}".format(float(cur_money) / (in_money+1) * 100)
    return render(request, 'home.html',{'income' : in_money ,'outcome' : out_money ,'in_percent': float(percent),'current_money' : cur_money,'gold' : cur_gold ,'stock' : interest_stock ,'sav' : top_bank_sav,'fixed' : top_bank_fixed})

def saving(request,user_name):
    if request.method == 'POST':
        Sav_list.objects.create(description=request.POST['description'],amount=int(request.POST['value']),sav_type=request.POST['type'],owner=user_name)
        return redirect('/%s/saving' %(user_name))

    items = Sav_list.objects.filter(owner=user_name)
    return render(request, 'saving.html',{'items': items,'user' : user_name})

def gold(request,user_name):
    gold_all = Gold_price.objects.all()
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
        #login(request,user)
        return redirect('/%s/' %(username))

    else:
        return HttpResponse("Error invaid login.")

def index(request):
    """xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {'charttype': charttype,'chartdata': chartdata,'chartcontainer': chartcontainer,'extra': {'x_is_date': False,'x_axis_format': '','tag_script_js': True,'jquery_on_ready': False,}}
    #return render_to_response('login.html', data)"""
    return render(request, 'login.html')

