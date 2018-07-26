from django import forms
from .models import Post
from django.contrib.auth import ( authenticate,
	get_user_model,
	login,
	logout,
	)

from .models import T_Model
class NPostForm(forms.Form):
	name=forms.CharField()
	email= forms.CharField()
	phone= forms.CharField()
	profession= forms.CharField()

class MPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'name',
			'email',
			'phone',
			'profession'
		] 

#login forms
User = get_user_model()#?

class UserLoginForm(forms.Form):
	username= forms.CharField()
	password= forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User 
		fields = [
			'username',
			'email',
			'password',
			'confirm_password',
		]
class T_Form(forms.ModelForm):
	class Meta:
		model = T_Model
		fields = ['name' ,'email','contact', 'city',]