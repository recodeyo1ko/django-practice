# Generated by Django 4.1 on 2024-07-12 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_initial'),
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'shopping_category',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('manufacturer', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=16)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('recomended', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.category')),
            ],
            options={
                'db_table': 'shopping_item',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_id', models.IntegerField(primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=256)),
                ('booked_date', models.DateTimeField()),
                ('cancel', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'db_table': 'shopping_purchase',
            },
        ),
        migrations.CreateModel(
            name='SearchItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('purchase_detail_id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.item')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.purchase')),
            ],
            options={
                'db_table': 'shopping_purchasedetail',
            },
        ),
        migrations.CreateModel(
            name='ItemsInCart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('booked_date', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'db_table': 'shopping_itemsincart',
            },
        ),
    ]
