from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)