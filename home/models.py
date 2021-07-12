from django.db import models
from django.core.exceptions import ImproperlyConfigured

# Create your models here.

class Contact(models.Model):
    sno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=13)
    feedback=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Message form'+self.name


