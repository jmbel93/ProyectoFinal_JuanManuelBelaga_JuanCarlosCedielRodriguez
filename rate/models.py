from django.db import models
from django.contrib.auth.models import User



class BookToRate(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    rate_date = models.DateField()
    description = models.TextField(blank = True, null=True)
    uploading_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f'{self.name} book --'