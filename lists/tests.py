from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTemplateUsed(response, 'lists/home.html')
