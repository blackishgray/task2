from django.urls import path 
from . import views  

app_name='product'

urlpatterns = [
	path('', views.productdata, name='productdata'),
	path('addproduct', views.addproduct, name='addproduct'),
	path('productprocess', views.productprocess, name='productprocess')
]

