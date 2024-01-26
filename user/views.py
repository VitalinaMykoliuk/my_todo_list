from django.contrib import auth
from django.contrib.auth import login
from django.urls import reverse
from django.views import View
from user.forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate


class MainUserView(View):
    template_name = 'dashboard/notes.html'
    template_name_2 = 'user/test.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.template_name_2)


class RegistrationUserView(View):
    template_name = 'user/register.html'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('notes:note'))
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})


class LoginUserView(View):
    template_name = 'user/login.html'

    def get(self, request):
        form = UserLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('notes:note'))
            else:
                print(form.errors)
        return render(request, self.template_name, {'form': form})



