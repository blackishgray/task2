from django.db import models
from django.contrib.auth.models import User, auth
from django.conf import settings

# Create your models here.

class PostModel(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content

