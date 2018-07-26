# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import NPostForm,MPostForm
from django.contrib.auth import ( authenticate,
	get_user_model,
	login,
	logout,
	)

from .forms import UserRegisterForm,UserLoginForm
from .forms import T_Form

from .models import T_Model
# Create your views here.
#normal form
def home(request):
	if request.user.is_authenticated():
		form= NPostForm(request.POST or None)
		if form.is_valid():
			name= form.cleaned_data.get('name')
			email=form.cleaned_data.get('email')
			phone=form.cleaned_data.get('phone')
			profession= form.cleaned_data.get('profession')

			instance = Post()
			instance.name=name
			instance.email=email
			instance.phone=phone
			instance.profession=profession
			instance.save()

			form = NPostForm()
	context = {
		'form':form
	}
	return render(request, "home.html", context)

#Model Form
def about(request):
	if request.user.is_authenticated():
		form = MPostForm(request.POST or None)
		if form.is_valid():
			new_post= form.save(commit=False)
			new_post=form.save()

			form=MPostForm()
	context = {
		'form':form
	}
	return render(request, "about.html", context)

def contactus(request):	
	if request.user.is_authenticated():
		return render(request, "contactus.html",{})


#website forms
def trip(request):
	form = T_Form(request.POST or None)
	if form.is_valid():
		new_post= form.save(commit=False)
		new_post=form.save()

		return redirect('/confirm/')
	context = {
		'form':form
	}
	return render(request, "trip.html", context)


#single,posts,edit,delete_v
def single(request ,id=None):
	if request.user.is_authenticated():
		instance=get_object_or_404(Post, id=id)
		context = {
			'instance':instance
		}
		return render(request, 'single.html', context)

def posts(request):
	if request.user.is_authenticated():
		query= Post.objects.all()
		context= {
			'obj_list':query
		}
		return render(request, 'posts.html', context)

def edit(request, id=None):
	if request.user.is_authenticated():
		ins=get_object_or_404(Post, id=id)#?
		form = MPostForm(request.POST or None,instance=ins)
		if form.is_valid():
			up_post = form.save(commit=False)
			up_post.save()
			return redirect('/single/'+id)
		context = {
			'form':form
		}
		return render(request, "edit.html", context)
def delete_v(request, id=None):
	if request.user.is_authenticated():
		instance=get_object_or_404(Post,id=id)	#?
		instance.delete()
		return redirect('/posts/')

#login views

def login_v(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		try:
			login(request, user)
			return redirect('/home/')
		except:
			return redirect('/register/')
	context = {
		'form':form
	}
	return render(request, 'login.html' ,context)

def register(request):
	form= UserRegisterForm(request.POST or None)
	if form.is_valid():
		usr= form.save(commit=False)
		password= form.cleaned_data.get('passsword')
		confirm_password= form.cleaned_data.get('confirm_password')
		if password == confirm_password:
			usr.set_password(password)
			usr.save()

		user= authenticate(username=usr.username, password=password)
		login(request,user)
		return redirect ('/home/')
	context = {
		'form':form
	}
	return render(request, 'register.html', context)

def logout_v(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('/')



#website views
def arun(request):
	return render(request, 'arun.html', {})

def index(request):
	return render(request, 'index.html', {})
def contact(request):
	return render(request, 'contact.html', {})
def confirm(request):
	return render(request, 'confirm.html',{})