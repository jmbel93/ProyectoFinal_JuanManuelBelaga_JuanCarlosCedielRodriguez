from django.db import models
from django.conf import settings
# Create your models here.
class About(models.Model):
    nombre =  models.CharField(max_length=100, verbose_name="nombre")
    descripcion =  models.TextField(verbose_name="descripcion")
    avatar = models.ImageField(upload_to='avatar',null=True,blank=True,verbose_name="avatar")
    user_creation =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.RESTRICT,related_name='user_creation',null=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True,blank=True)