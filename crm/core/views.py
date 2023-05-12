from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class Home(TemplateView):
    template_name = 'home.html'


class Company(TemplateView):
    template_name = 'company.html'

class CreateCompany(TemplateView):
    template_name = 'create_company.html'

class CreateUser(TemplateView):
    template_name = 'create_user.html'

class Login(TemplateView):
    template_name = 'login.html'

class Main(TemplateView):
    template_name = 'main.html'

class Users(TemplateView):
    template_name = 'users.html'


