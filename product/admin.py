from django.contrib import admin

# Register your models here.
from .models import ProductModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'product_weight', 'product_price', 'created_at', 'updated_at')

	using = 'product_db'

	def get_queryset(self, request):
		return super().get_queryset(request).using(self.using)

	def save_model(self, request, obj, form, change):
	    obj.save(using=self.using)

	def delete_model(self, request, obj):
	    obj.delete(using=self.using)


# admin.site.register(ProductModel, ProductModelAdmin)
