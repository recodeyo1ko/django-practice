from django.db import models
from account.models import AccountUser

# Create your models here.
class ShoppingCategory(models.Model):
  class Meta:
        db_table = 'shopping_category'

  category_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=256)


class ShoppingItem(models.Model):
  class Meta:
        db_table = 'shopping_item'
  item_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=128)
  manufacturer = models.CharField(max_length=32)
  color = models.CharField(max_length=16)
  price = models.IntegerField(max_length=11)
  stock = models.IntegerField(max_length=11)
  recomended = models.IntegerField(max_length=1)
  category = models.ForeignKey(ShoppingCategory, on_delete=models.CASCADE)


class ShoppingItemsincart(models.Model):
  class Meta:
        db_table = 'shopping_itemsincart'

  id = models.IntegerField(primary_key=True)
  amount = models.IntegerField(max_length=11)
  booked_date = models.DateTimeField()
  item = models.ForeignKey(ShoppingItem, on_delete=models.CASCADE)
  user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)


class ShoppingPurchase(models.Model):
  class Meta:
        db_table = 'shopping_purchase'

  purchase_id = models.IntegerField(primary_key=True)
  destination = models.CharField(max_length=256)
  booked_date = models.DateTimeField()
  cancel = models.IntegerField(max_length=1)
  user = models.ForeignKey(AccountUser, on_delete=models.CASCADE)

class ShoppingPurchasedetail(models.Model):
  class Meta:
        db_table = 'shopping_purchasedetail'

  purchase_detail_id = models.IntegerField(primary_key=True)
  amount = models.IntegerField(max_length=11)
  item = models.ForeignKey(ShoppingItem, on_delete=models.CASCADE)
  purchase = models.ForeignKey(ShoppingPurchase, on_delete=models.CASCADE)
