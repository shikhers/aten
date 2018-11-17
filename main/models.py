from django.db import models
from django.utils import timezone

#Models for the main page
class Mainpage(models.Model):
    #For product title.....
    productTitle = models.CharField(max_length=200)
    #For product image url to insert image
    productImageUrl = models.CharField(max_length=500)
    #Date for To make post Upper to lower
    date = models.DateTimeField(default=timezone.now)
    #For product details about the detail
    productDetail = models.TextField()
    #About the product work
    productWork = models.CharField(max_length=200)
