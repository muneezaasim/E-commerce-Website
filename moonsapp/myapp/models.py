from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class orders(models.Model):
    orderID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    shipping_method = models.CharField(max_length=20, default='standard')  # Provide a default value
    payment_option = models.CharField(max_length=20, default='standard')
  