from django.db import models

# Create your models here.
class Customer(models.Model):
    c_name = models.CharField(max_length = 50)
    c_email = models.CharField(max_length = 50)
    c_mobile = models.CharField(max_length = 30)
    c_password = models.CharField(max_length = 20, default='')

    class Meta:
        db_table = 'customer'


class Seller(models.Model):
    s_name = models.CharField(max_length=50)
    s_email = models.CharField(max_length = 50)
    s_mobile = models.CharField(max_length = 30)
    s_password = models.CharField(max_length = 20, default='')

    class Meta:
        db_table = 'seller'




