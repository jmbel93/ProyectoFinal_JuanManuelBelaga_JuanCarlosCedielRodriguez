from django.db import models
from ckeditor.fields import RichTextField



class CatalogueBook(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publication_date = models.DateField(null=True, blank=True)
    description = RichTextField(blank = True, null=True)
    imagen = models.ImageField(upload_to='images_book',null=True,blank=True,verbose_name="image")

  


    def __str__(self):
        return f'libro: {self.name}'