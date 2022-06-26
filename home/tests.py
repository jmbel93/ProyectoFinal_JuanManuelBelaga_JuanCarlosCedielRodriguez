from django.test import TestCase
from home.models import CatalogueBook

class CatalogueBookTestCase(TestCase):
    def test_date(self):
        # CatalogueBook.objects.create(publication_date = "1933-10-14")
        # CatalogueBook.objects.create(publication_date = "19-1011-14")
        CatalogueBook.objects.create(description = 1-1)


