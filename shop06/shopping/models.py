from django.db import models
from account.models import User

# Create your models here.
class Category(models.Model):
  class Meta:
        db_table = 'shopping_category'

  category_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=256)

class SearchItem(models.Model):
    pass

class Item(models.Model):
  class Meta:
        db_table = 'shopping_item'
  item_id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=128)
  manufacturer = models.CharField(max_length=32)
  color = models.CharField(max_length=16)
  price = models.IntegerField()
  stock = models.IntegerField()
  recomended = models.IntegerField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ItemsInCart(models.Model):
  class Meta:
        db_table = 'shopping_itemsincart'

  id = models.IntegerField(primary_key=True)
  amount = models.IntegerField()
  booked_date = models.DateTimeField()
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class Purchase(models.Model):
  class Meta:
        db_table = 'shopping_purchase'

  purchase_id = models.IntegerField(primary_key=True)
  destination = models.CharField(max_length=256)
  booked_date = models.DateTimeField()
  cancel = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class PurchaseDetail(models.Model):
  class Meta:
        db_table = 'shopping_purchasedetail'

  purchase_detail_id = models.IntegerField(primary_key=True)
  amount = models.IntegerField()
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
