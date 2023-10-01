from django.db import models
from django.db.models import JSONField
type_of_customer = [
    ('new', 'New Customer'),
    ('return', 'Return Customer'),
    ('private', 'Private'),
]


class Customer(models.Model):
    date=models.DateField()
    fname = models.CharField(max_length=50)
    lname =  models.CharField(max_length=50)
    customer_id=models.IntegerField()
    mail = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    customer_type = models.CharField(max_length=15, choices=type_of_customer)
    product_table = JSONField(default=dict)
    totalbuys= models.FloatField()

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class SalesHistory(models.Model):
    date = models.DateField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    customer_id = models.IntegerField()
    customer_type = models.CharField(max_length=15, choices=type_of_customer)
    sales_man= models.CharField(max_length=20)
    price = models.JSONField(default=dict)
    product_table = models.JSONField(default=dict)
    final_prize = models.FloatField()
    profit=models.FloatField()

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Equipment(models.Model):
    product_type = models.CharField(max_length=100)
    over_all_stock= models.IntegerField()
    cost=models.FloatField()
    price_for_private= models.FloatField()
    price_for_drivers= models.FloatField()
    current_stock=models.IntegerField()
    notice=models.IntegerField()
    origin_product=models.CharField(max_length=100)
    package=models.IntegerField()
    
    def __str__(self):
        return f"{self.product_type}"
    
class workers(models.Model):
    fname = models.CharField(max_length=50)
    lname =  models.CharField(max_length=50)
    new_customer = JSONField(default=dict ,null=True)
    return_customers=JSONField(default=dict,null=True)
    sum_of_sales=JSONField(default=dict,null=True)
    bounus=JSONField(default=dict,null=True)
    def __str__(self):
            return f"{self.fname}"
