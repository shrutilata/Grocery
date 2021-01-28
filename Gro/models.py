from django.db import models
from django.contrib.auth.models import User

class list1(models.Model):
    iname = models.CharField(max_length=255,blank=True)
    quant = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=255,blank=True)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.iname