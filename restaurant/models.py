from django.db import models

# Create your models here.

class kitchen(models.Model):
    kitchen_name = models.CharField(max_length=200)
    enter_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()

    qty = models.IntegerField()
    total_kitchen_wise_amt = models.FloatField()

class category(models.Model):
    category_name = models.CharField(max_length=200)
    enter_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()

class resturant_items(models.Model):
    name=models.CharField(max_length=200)
    price = models.IntegerField()
    item_category = models.CharField(max_length=200)
    kitchen_nam = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_bys = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()

    qty = models.IntegerField()
    total_item_wise_amt = models.FloatField()

class bills_no(models.Model):
    billing_no = models.IntegerField()

class table_order_no(models.Model):
    table_order_nos = models.IntegerField()

class temp_billing(models.Model):
    bill_no = models.IntegerField()
    particulars = models.CharField(max_length=200)
    price = models.IntegerField()
    qty = models.IntegerField()
    amount = models.FloatField()
    kitchen = models.CharField(max_length=200)

    type = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    item_catergory = models.CharField(max_length=200)
    description = models.TextField()

    table_name = models.CharField(max_length=200)

    day = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    enter_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()
    billed_by = models.CharField(max_length=200)
