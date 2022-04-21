from django.shortcuts import render
from market.models import *
# Create your views here.
# def stationery(request):
# 	rec = Product.objects.filter(category_id=1)
# 	header = 'stationery'
# 	#namecat = Category.objects.get(category_id=1).name
# 	return render(request, 'market/main.html', {'recommend': 'rec', 'header': 'stationery'})

# def tech(request):
# 	rec = Product.objects.filter(category_id=2)
# 	header = 'tech'
# 	return render(request, 'market/main.html', {'recommend': 'rec', 'header': 'tech'})

cat = Category.objects.all()

def main(request):
	
	rec = Product.objects.all()
	header = 'best products'
	context = {
		'recommend': rec,
		'categories': cat,
		'header': header
	}
	return render(request, 'market/main.html', context)

def category(request, cat_id):
	rec = Product.objects.filter(pk = cat_id)
	header = Category.objects.get(pk = cat_id).name
	context = {
		'categories':cat,
		'recommend': rec,
		'header': header
	}
	return render(request, 'market/main.html', context)

def product(request, product_id):
	product = Product.objects.get(pk = product_id)
	context = {
		'name': product.name,
		'price': product.price,
		'description': product.description,
		'quantity': product.quantity,

		'categories': cat
	}
	return render(request, 'market/product.html', context)