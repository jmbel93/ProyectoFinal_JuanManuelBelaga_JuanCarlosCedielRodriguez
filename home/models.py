from django.db import models



class CatalogueBook(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publication_date = models.DateField()
    description = models.TextField(blank = True, null=True)
  


    def __str__(self):
        return f'libro: {self.name}'