from main.models import Item
from django.test import TestCase


class TestModel(TestCase):

    def setUp(self):
        self.item1 = Item.objects.create(
            name='nature',
            image='image1'
        )

    def test_should_create_item(self):
        photo = self.item1
        photo.save()
        self.assertEqual(str(photo), 'nature')

