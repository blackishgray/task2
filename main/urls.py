from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'main'

#set urls path for the app
urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('post_form', views.post_form, name='post_form'),
	path('post_data', views.post_data, name='post_data'),
]
