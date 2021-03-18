import re

from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, RegistrationForm
from .models import EmailConfirmed

from django.contrib import messages
from django.urls import reverse


def logout_view(request):
	logout(request)
	messages.success(request, "Successfully logout. Now login again")
	return HttpResponseRedirect('%s'%(reverse("auth_login")))



def login_view(request):
	form = LoginForm(request.POST or None)
	btn = "Login"

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']

		user = authenticate(username=username, password=password)
		login(request,user)
		messages.success(request, "Successfully Login Welcom Back")
		return HttpResponseRedirect("/")

	context = {
		"form":form,
		"submit_btn": btn,
	}
	return render(request, "form.html", context)


def registration_view(request):
	form = RegistrationForm(request.POST or None)
	btn = "Join"
	if form.is_valid():
		new_user = form.save(commit=False)
		# new_user.firstname = "Al"
		new_user.save()
		messages.success(request, "Successfully Registered. Plesse Confirm Your Email now.")
		return HttpResponseRedirect("/")
		# username = form.cleaned_data['username']
		# password = form.cleaned_data['password']

		# user = authenticate(username=username, password=password)
		# login(request,user)		


	context = {
		"form":form,
		"submit_btn": btn,
	}
	return render(request, "form.html", context)

SHA1_RE = re.compile('^[a-f0-9]{40}$')

def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		print("Activation Key is Raal")
		try:
			instance = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			instance = None
			raise Http404
		if instance is not None and not instance.confirmed:
			page_message = "Confirmation Successfull! Welcome."
			instance.confirmed = True
			instance.activation_key="Confirmed"
			instance.save()
		elif instance is not None and instance.confirmed:
			page_message = "Already Confirmed"
		else:
			page_message = ""

		context = {"page_message": page_message}
		return render(request, "accounts/activation_complete.html", context)

	else:
		raise Http404

