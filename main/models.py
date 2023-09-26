from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)