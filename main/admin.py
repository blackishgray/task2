from django.contrib import admin
from .models import PostModel
# Register your models here.

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
	list_display = ('user', 'content', 'created_at', 'updated_at')
