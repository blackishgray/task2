from django.shortcuts import render
from django.http import JsonResponse

from .models import ProductModel
from .forms import ProductForm

# Create your views here.
def productdata(request):
	product_data = ProductModel.objects.using('product_db').all()
	mydict = {
		'product_data' : product_data
	}
	return render(request, 'product_data.html', context=mydict)

def addproduct(request):
	form = ProductForm()
	myform = {
		'form':form
	}
	return render(request, 'addproduct.html', context=myform)

def productprocess(request):
	print(request.method)
	if request.method=='POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			print('Inside If')
			product_name = request.POST['product_name']
			product_weight = request.POST['product_weight']
			product_price = request.POST['product_price']
			pm = ProductModel(product_name=product_name, product_weight=product_weight, product_price=product_price)
			pm.save()
			return JsonResponse({'status':1})
		else:
			return JsonResponse({'status':0})
