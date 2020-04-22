from django.db import models
from django.urls import reverse

class Submit(models.Model):
    Username = models.CharField(max_length=300)
    Mail = models.CharField(max_length=300)
    Password = models.CharField(max_length = 300)
    Phone = models.CharField(max_length =10)
    FirstName = models.CharField(max_length=300)
    LastName = models.CharField(max_length=300)
    
    class Meta:  
        db_table = "Register"
