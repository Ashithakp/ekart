from django.db import models

# Create your models here.

class Seller(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    company_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    profile_picture = models.ImageField(upload_to="seller/")
    login_id = models.IntegerField(null=True)
    account_number = models.BigIntegerField()
    bank_name = models.CharField(max_length = 20)
    branch_name = models.CharField(max_length = 20)
    ifsc_code = models.CharField(max_length = 20)
    status = models.CharField(max_length = 50, default = 'pending')

    class Meta:
        db_table = 'seller_tb'