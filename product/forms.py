from django import forms
from .models import ProductModel

# Ṃodel form for products
class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductModel
		fields=['product_name', 'product_weight', 'product_price']
		widgets = {
			'product_name':forms.TextInput(attrs={'id':'product_name', 'class':'form-control', 'placeholder':'Earphones'}),
			'product_weight':forms.NumberInput(attrs={'id':'product_weight', 'class':'form-control', 'placeholder':'120gms'}),
			'product_price':forms.NumberInput(attrs={'id':'product_price', 'class':'form-control', 'placeholder':'1200/-'}),
		}
