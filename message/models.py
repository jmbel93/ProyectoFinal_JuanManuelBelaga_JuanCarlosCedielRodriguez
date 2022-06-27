from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from home.models import CatalogueBook
from ckeditor.fields import RichTextField



class Comentario(models.Model):
    titulo_del_comentario = models.CharField(max_length=40)
    comment_date = models.DateTimeField(default=datetime.now)
    comentario = RichTextField(blank = True, null=True)
    autor_del_comentario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    libro_comentado = models.ForeignKey(CatalogueBook, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f'{self.libro_comentado}'
