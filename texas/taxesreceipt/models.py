from django.db import models
from django.db.models.base import Model

# Create your models here.
class customer(models.Model):
    id = models.CharField(primary_key=True,max_length=300)
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=2)
    governorate = models.CharField(max_length=300)
    region_city = models.CharField(max_length=300)
    tax_number_id = models.CharField(max_length=20)
    street = models.CharField(max_length=300)
    building_number = models.CharField(max_length=300)
    type = models.CharField(max_length=1)

class invoice(models.Model):
    internal_id = models.CharField(primary_key=True,max_length=300)
    document_type = models.CharField(max_length=1)
    date_time_issued = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=3)
    currency_rate = models.DecimalField(decimal_places=12,max_digits=28)
    extra_discount_amount = models.DecimalField(decimal_places=12,max_digits=28)
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE ,default=1)

class invoice_line(models.Model):
    id = models.CharField(primary_key=True,max_length=300)
    internal_code = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    quantity = models.FloatField()
    amount = models.FloatField()
    unit = models.CharField(max_length=10)
    taxes = models.CharField(max_length=2)
    rates = models.IntegerField()
    discount = models.FloatField()
    sub_taxes = models.CharField(max_length=4)
    value_difference = models.FloatField()
    invoice_id = models.ForeignKey(invoice ,on_delete=models.CASCADE , default=1)

class invoice_result(models.Model):
    id = models.CharField(primary_key=True,max_length=300)
    uu_id = models.CharField(max_length=30)
    submission_uu_id = models.CharField(max_length=30)
    state = models.IntegerField()
    errors = models.CharField(max_length=1000)
    invoice_id = models.ForeignKey(invoice ,on_delete=models.CASCADE , default=1)


