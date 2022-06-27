from django.test import TestCase
from rate.models import BookToRate

class CatalogueBookTestCase(TestCase):
    def test_rate(self):
        BookToRate.objects.create(name = "1933-10-14")


