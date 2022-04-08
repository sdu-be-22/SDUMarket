from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Customer(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	mobile_num = models.CharField(max_length=50)
	email = models.EmailField()		
	login = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

class Employee(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	salary = models.IntegerField()

class Card(models.Model):
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	card_num = models.BigIntegerField()

class Payment(models.Model):
	payment_amount = models.BigIntegerField()
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
	card_id = models.ForeignKey(Card, on_delete=models.CASCADE)



class Category(models.Model):
	name = models.CharField(max_length=255)

class Item(models.Model):
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)

class Product(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.CharField(max_length=255)
	quantity = models.IntegerField()
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

class Profit(models.Model):
	sold_number = models.IntegerField()
	sold_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	profit = models.BigIntegerField()

class Order(models.Model):
	date = models.DateField(auto_now_add=True)
	payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	payment_amount = models.IntegerField()

class tbl_Authentication(models.Model):
    Empcode = models.IntegerField()
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    is_active = models.IntegerField(null=True)
 
    def __str__(self):
        return self.username
 
    empAuth_objects = models.Manager()
class Topic(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Room(models.Model):
	host = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
	topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
	name = models.CharField(max_length= 200)
	description = models.TextField(null=True, blank=True)
	participants = models.ManyToManyField(
		User, related_name = 'participants',blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name

	class Meta: 
		ordering = ['-updated', '-created']




class Message(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	room = models.ForeignKey(Room, on_delete = models.CASCADE)
	body = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.body[0:50]

	
	


	






