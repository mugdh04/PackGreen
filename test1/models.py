from django.db import models
import datetime

class Product(models.Model):
    Product_ID = models.CharField(max_length=30, unique=True)
    Product_Name = models.CharField(max_length=30)
    Product_Description = models.CharField(max_length=400)
    Product_Category = models.CharField(max_length=100)
    Product_Image = models.ImageField(upload_to='Image/')
    def __str__(self):
        return self.Product_Name
    
class Contact_Query(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    date_time = models.DateTimeField(("Date"), default=datetime.datetime.today)
    def __str__(self):
        return self.email