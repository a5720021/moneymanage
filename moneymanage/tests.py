from django.core.urlresolvers import resolve
from django.test import TestCase
from moneymanage.views import home,saving,gold,stock,bank,index,login
from django.template.loader import render_to_string
from django.http import HttpRequest,HttpResponse
import re
from moneymanage.models import Sav_list,Gold_price,Stock,Bank
from django.contrib.auth.models import User

class HomePageTest(TestCase):

    #Function for decoding CSRF from POST method
    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    #Test homepage render login page correct
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('login.html')
        self.assertEqual(self.remove_csrf(response.content.decode()), expected_html)

class GoldModelTest(TestCase):

    #Test gold can save in database
    def test_saving_and_retrieving_items(self):
        first_gold = Gold_price(buy_price=25000,sell_price='24000')
        first_gold.save()

        all_gold = Gold_price.objects.all()
        self.assertEqual(all_gold.count(), 1)

        self.assertEqual(all_gold[0].buy_price, 25000)

class StockModelTest(TestCase):

    #Test stock data can save in databases
    def test_saving_and_retrieving_items(self):
        Stock.objects.create(name='TES',value=2400,change=5.2)
        Stock.objects.create(name='CPA',value=1500,change=-2.5)

        stock = Stock.objects.all()
        self.assertEqual(stock.count(), 2)

        self.assertEqual(stock[0].value, 2400)

class BankModelTest(TestCase):

    #Test bank interest data can save in databases
    def test_saving_and_retrieving_items(self):
        Bank.objects.create(name='Kasikorn',fixed_min=0.6,fixed_max=1.2,saving=0.5)
        Bank.objects.create(name='Krungsri',fixed_min=0.5,fixed_max=1.4,saving=0.6)

        bank = Bank.objects.all()
        self.assertEqual(bank.count(), 2)

        self.assertEqual(bank[0].fixed_max, 1.2)

class SavModelTest(TestCase):

    #Function for decoding CSRF from POST method
    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    #Test Saving data can save in databases
    def test_saving_and_retrieving_items(self):
        first_sav = Sav_list(description='Test Saving',amount=7000,sav_type='income')
        first_sav.save()

        saved_items = Sav_list.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.description, 'Test Saving')

    #Test saving data can save and show correct data
    def test_sav_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['type'] = 'income'
        request.POST['value'] = '5000'
        request.POST['description'] = 'won lottery'
        user = User.objects.create_user("test", "test@test.com", "Test1234")
        user.save()

        response = saving(request,"test")

        self.assertEqual(Sav_list.objects.count(), 1)
        new_item = Sav_list.objects.first()
        self.assertEqual(new_item.description, 'won lottery')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/test/saving')

    #Test Saving page render correct when don't add to databases
    def test_sav_only_saves_items_when_necessary(self):
        request = HttpRequest()
        saving(request,"test")
        self.assertEqual(Sav_list.objects.count(), 0)

class AccountTest(TestCase):

    #Test account data can save data correctly (in databases)
    def test_account_created(self):
        user = User.objects.create_user("test", "test@test.com", "Test1234")
        user.save()
        user2 = User.objects.create_user("test2", "test2@test.com", "Test123456")
        user2.save()
        userall = User.objects.all()
        first_saved_item = userall[0]
        self.assertEqual(first_saved_item.email, 'test@test.com')

