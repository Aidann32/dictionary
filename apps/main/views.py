from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import NewUserForm, KazakhAuthenticationForm


def logout_request(request):
	logout(request)
	messages.info(request, "Сіз жүйеден сәтті шықтыңыз.") 
	return redirect("login")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Тіркеу сәтті өтті." )
			return redirect("main_page")
		messages.error(request, "Тіркелу сәтсіз аяқталды. Қате ақпарат.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = KazakhAuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Енді сіз {username} логинімен кірдіңіз.")
				return redirect("main_page")
			else:
				messages.error(request,"Логин немесе құпия сөз дұрыс емес.")
		else:
			messages.error(request,"Логин немесе құпия сөз дұрыс емес.")
	form = KazakhAuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})