from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)

class Item(models.Model):
	name = models.CharField(max_length=255)
	category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.TextField(blank=True)
	quantity = models.IntegerField()
	category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
	item = models.ForeignKey('Item', on_delete=models.PROTECT, null=True)



	