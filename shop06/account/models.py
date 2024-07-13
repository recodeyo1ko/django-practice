from django.db import models

# Create your models here.

class User(models.Model):
  class Meta:
        db_table = 'account_user'

  user_id = models.IntegerField(primary_key=True)
  password = models.CharField(max_length=256)
  name = models.CharField(max_length=128)
  address = models.CharField(max_length=256)

class Admin(models.Model):
  class Meta:
        db_table = 'administrator_admin'
