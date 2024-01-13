from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForms, UserLoginForms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.

class UserRegisterationView(View):
    form_class = UserRegisterationForms
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create(request, cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'Register done!', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = UserLoginForms
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, usename=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'login successfully', 'success')
                return redirect('home:home')
            messages.error(request, 'Username Or Password Is Wrong', 'warring')
        return render(request, self.template_name, {'form': form})
