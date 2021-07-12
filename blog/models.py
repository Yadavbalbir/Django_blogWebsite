from django.db import models
from django.core.exceptions import ImproperlyConfigured
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    sno=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=256)
    content=models.TextField()
    author=models.CharField(max_length=250)
    slug=models.CharField(max_length=130)
    timestamp=models.DateTimeField(timezone.now())
    def __str__(self):
        return self.title+' by'+self.author
