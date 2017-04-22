from django.core.urlresolvers import resolve
from django.test import TestCase
from moneymanage.views import home,saving
from django.template.loader import render_to_string
from django.http import HttpRequest,HttpResponse
import re
from moneymanage.models import Sav_list

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

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

    """def test_sav_returns_correct_html(self):
        request = HttpRequest()
        response = saving(request)
        expected_html = render_to_string('saving.html')
        self.assertEqual(self.remove_csrf(response.content.decode()), expected_html)

    def test_saving_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['description'] = 'test'
        response = saving(request)
        self.assertIn('test', self.remove_csrf(response.content.decode()))
        expected_html = render_to_string('saving.html',{'new_sav_list':  'test'})
        self.assertEqual(self.remove_csrf(response.content.decode()), expected_html)"""

class ModelTest(TestCase):

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



