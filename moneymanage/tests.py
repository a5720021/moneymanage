from django.core.urlresolvers import resolve
from django.test import TestCase
from moneymanage.views import home_page,saving
from django.template.loader import render_to_string
from django.http import HttpRequest,HttpResponse
import re

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class SavingTest(TestCase):

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_uses_saving_template(self):
        response = self.client.get('http://localhost:8000/saving')
        self.assertTemplateUsed(response, 'saving.html')

    def test_sav_returns_correct_html(self):
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
        self.assertEqual(self.remove_csrf(response.content.decode()), expected_html)


