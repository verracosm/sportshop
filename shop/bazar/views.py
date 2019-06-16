from django.shortcuts import render, get_object_or_404, redirect
from .models import Baskecior, ProductCategory, Product, Order
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

def home(request):
	products = Product.objects.all()

	context = {
		'produkt': products
	}

	return render(request, 'index.html', context)

@login_required
def baskecior(request):
	koszykor = Baskecior.objects.filter(user=request.user)

	context = {
		'koszyk': koszykor
	}

	return render(request, 'koszyk.html', context)


@login_required
def add_to_basket(request, pk):
	product = get_object_or_404(Product, pk=pk)
	data = {'empty': False}

	if product.amount > 0:
		try:
			baskeciorek = Baskecior.objects.get(user=request.user, product=product)
			if baskeciorek.amount < product.amount:
				baskeciorek.amount += 1
				baskeciorek.save()
				return JsonResponse(data)
			else:
				data = {}
				data['empty'] = True
				print(data)
				return JsonResponse(data)
		except:
			Baskecior.objects.update_or_create(user = request.user, product = product)
			return JsonResponse(data)
	else:
		data['empty'] = True
		return JsonResponse(data)


@login_required
def delete_basket(request):
	basket = Baskecior.objects.filter(user=request.user).delete()
	return HttpResponse(status=204)


@login_required
def add_order(request):
	basket = Baskecior.objects.filter(user=request.user)

	if basket:
		Order.objects.filter(user=request.user).delete()
		for baskecior in basket:
			Order.objects.update_or_create(user=request.user, product=baskecior.product, amount=baskecior.amount)

		Baskecior.objects.filter(user=request.user).delete()

	return HttpResponse(status=204)


@login_required 
def orders(request):
	orders = Order.objects.filter(user=request.user)

	context = {
		'orders': orders
	}

	return render(request, 'orders.html', context)
