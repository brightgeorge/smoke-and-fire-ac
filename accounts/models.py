from django.db import models

# Create your models here.


######## ACCOUNTS START HERE ##############

class table1(models.Model):
    name=models.CharField(max_length=200)
    item_category = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_bys = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()

class in_exp_items_daily(models.Model):
    particulars = models.CharField(max_length=200)
    amount = models.FloatField()
    ledger = models.CharField(max_length=200)
    accounts_book_name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    item_catergory = models.CharField(max_length=200)
    description = models.TextField()
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

    def aug_income(self):
        queryset = in_exp_items_daily.objects.filter(month='08', type='income')
        totals = queryset.aggregate(sum=Sum('amount'))
        return totals


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

class opening_balance(models.Model):
    month_no = models.CharField(max_length=200)
    month_name = models.CharField(max_length=200)
    month_amount = models.FloatField()
    date = models.CharField(max_length=200)
    enter_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()

class ledger(models.Model):
    ledger_name = models.CharField(max_length=200)
    contact_person_name = models.CharField(max_length=200)
    contact_person_mob = models.CharField(max_length=200)
    address = models.TextField()
    created_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()

class accounts_book(models.Model):
    accounts_book_name = models.CharField(max_length=200)
    #details = models.TextField()
    created_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()


######## ACCOUNTS END EHERE ####################

class share_holders(models.Model):
    share_holders_name = models.CharField(max_length=200)
    share_holders_percentage = models.CharField(max_length=200)
    share_holders_amt = models.CharField(max_length=200)

    created_by = models.CharField(max_length=200)
    cb_date = models.CharField(max_length=200)
    updated_by = models.CharField(max_length=200)
    ub_date = models.CharField(max_length=200)
    deleted_by = models.CharField(max_length=200)
    db_date = models.CharField(max_length=200)
    ub_flag = models.IntegerField()
    flag = models.IntegerField()


class background_color(models.Model):
    theme_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    flag = models.CharField(max_length=200)
