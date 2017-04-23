from django.core.urlresolvers import resolve
from django.test import TestCase
from moneymanage.views import home,saving,gold
from django.template.loader import render_to_string
from django.http import HttpRequest,HttpResponse
import re
from moneymanage.models import Sav_list,Gold_price

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    """def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)"""

    def test_home_can_display_saving(self):
        Sav_list.objects.create(description='Test Saving',amount=7000,sav_type='income')
        request = HttpRequest()
        response = home(request)

        self.assertIn('7000',response.content.decode())

class SavingTest(TestCase):

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_uses_saving_template(self):
        response = self.client.get('http://localhost:8000/saving')
        self.assertTemplateUsed(response, 'saving.html')

    def test_sav_displays_all_list_items(self):
        Sav_list.objects.create(description='Testsaving 1')
        Sav_list.objects.create(description='Testsaving 2')

        request = HttpRequest()
        response = saving(request)

        self.assertIn('Testsaving 1', self.remove_csrf(response.content.decode()))
        self.assertIn('Testsaving 2', self.remove_csrf(response.content.decode()))

class GoldPageTest(TestCase):

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_uses_saving_template(self):
        response = self.client.get('http://localhost:8000/gold')
        self.assertTemplateUsed(response, 'gold.html')

    def test_gold_displays_all_list_items(self):
        Gold_price.objects.create(buy_price=25000,sell_price='24000')
        Gold_price.objects.create(buy_price=24500,sell_price='23500')

        request = HttpRequest()
        response = gold(request)
        print self.remove_csrf(response.content.decode())
        self.assertIn('25000', self.remove_csrf(response.content.decode()))
        self.assertIn('24500', self.remove_csrf(response.content.decode()))

class GoldModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_gold = Gold_price(buy_price=25000,sell_price='24000')
        first_gold.save()

        all_gold = Gold_price.objects.all()
        self.assertEqual(all_gold.count(), 1)

        self.assertEqual(all_gold[0].buy_price, 25000) 

class SavModelTest(TestCase):

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_saving_and_retrieving_items(self):
        first_sav = Sav_list(description='Test Saving',amount=7000,sav_type='income')
        first_sav.save()

        saved_items = Sav_list.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.description, 'Test Saving')

    def test_sav_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['type'] = 'income'
        request.POST['value'] = '5000'
        request.POST['description'] = 'won lottery'

        response = saving(request)

        self.assertEqual(Sav_list.objects.count(), 1)
        new_item = Sav_list.objects.first()
        self.assertEqual(new_item.description, 'won lottery')
    
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/saving')

    def test_sav_only_saves_items_when_necessary(self):
        request = HttpRequest()
        saving(request)
        self.assertEqual(Sav_list.objects.count(), 0)



