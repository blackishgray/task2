from django.db import models

# Create your models here.
class ProductModel(models.Model):
	product_name = models.CharField(max_length=200)
	product_weight = models.IntegerField()
	product_price = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product_name