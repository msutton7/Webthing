from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from . import models
from . import forms

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

#def test(request):
#	if request.method == 'POST':
#		CustomUser.age += 1
		
def request_page(request):
	if(request.GET.get('mybtn')):
		mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
		return render(request,'myApp/templateHTML.html')

