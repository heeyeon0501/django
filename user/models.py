from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model) :
    
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    created_date=models.DateTimeField(default=timezone.now)
    birthday = models.DateTimeField(default=timezone.now)
 

    def __str__(self) :
        return self.name