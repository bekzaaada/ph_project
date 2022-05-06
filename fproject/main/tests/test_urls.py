from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import index, gallery

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_gallery_url_is_resolves(self):
        url = reverse('gallery')
        self.assertEqual(resolve(url).func, gallery)

