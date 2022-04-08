from django.shortcuts import render
from market.models import *
# Create your views here.
def stationery(request):
	rec = Product.objects.filter(category_id=1)
	header = 'stationery'
	#namecat = Category.objects.get(category_id=1).name
	return render(request, 'market/main.html', {'recommend': 'rec', 'header': 'stationery'})

def tech(request):
	rec = Product.objects.filter(category_id=2)
	header = 'tech'
	return render(request, 'market/main.html', {'recommend': 'rec', 'header': 'tech'})

def main(request):
	rec = Product.objects.all()
	header = 'best products'
	return render(request, 'market/main.html', {'recommend': 'rec', 'header': 'best products'})

def product(request):
	prdata = request.GET
	context = {
		'name': prdata['name'],
		'price': prdata['price'],
		'description': prdata['description']
	}
	print(prdata)
	return render(request, 'market/product.html', context=context)