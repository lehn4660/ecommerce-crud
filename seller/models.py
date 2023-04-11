from django.db import models

from common.models import Seller

# Create your models here.

class AddProducts(models.Model):
    category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    product_stock = models.IntegerField()
    product_price = models.FloatField()
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',default='')

    class Meta:
        db_table = 'addproducts'
