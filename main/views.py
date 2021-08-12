from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import JsonResponse

from .models import PostModel
from .forms import PostForm

# Create your views here.
def index(request):
	post_data = PostModel.objects.using('default').all().order_by('-id')
	mydict = {
		'post_data':post_data,
	}
	return render(request, 'index.html', context = mydict)

# funtion to grab post data
# from database
def post_form(request):
	form = PostForm()
	data = PostModel.objects.all()
	dict2 = {
		'form':form,
	}
	return render(request, 'post_form.html', context=dict2)

# funtion to save post data
def post_data(request):
	print(request.method)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			print('Inside If')
			content = request.POST['content']
			# create an instance of the form
			instance = form.save(commit=False)
			# check whether the request user and the
			# form user instance is same
			instance.user = request.user
			instance.save()
			return JsonResponse({'status':1})
		else:
			return JsonResponse({'status':0})

# function to register the user
def register(request):
	if request.method == 'POST':
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		username = request.POST['username']

		if password1==password2:

			# filter the username for any duplicates in the table
			if User.objects.filter(username=username).exists():
				mes = 'Username Already Exists'
				return JsonResponse({'status':0, 'messages':mes})

			# filter emails
			elif User.objects.filter(email=email).exists():
				mes = 'Email Already Exists'
				return JsonResponse({'status':0, 'messages':mes})

			else:
				user = User.objects.create_user(username=username, password=password2,
					email=email, first_name=first_name, last_name=last_name)
				user.save()
				# messages.info(request, 'User created')
				print('User created')
				return JsonResponse({'status':1})

		else:
			mes  = 'Password Does not match.'
			return JsonResponse({'status':0, 'messages':mes})

	else:
		return render(request, 'register.html')

# login function
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return JsonResponse({'status' : 1})
		else:
			mes = 'Invalid credentials'
			return JsonResponse({'status':0, 'message':mes})
	else:
		return render(request, 'login.html')

# logout function
def logout(request):
	auth.logout(request)
	return redirect('main:index')
