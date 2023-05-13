from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import time


class CustomHtmxMixin:
    def dispatch(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        self.template_htmx = self.template_name
        if not self.request.META.get('HTTP_HX_REQUEST'):
            self.template_name = 'components/include_block.html'
        else:
            time.sleep(1)
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        kwargs['template_htmx'] = self.template_htmx
        return super().get_context_data(**kwargs)


class Home(TemplateView):
    template_name = 'home.html'


class Company(CustomHtmxMixin, TemplateView):
    template_name = 'company.html'

class CreateCompany(CustomHtmxMixin, TemplateView):
    template_name = 'create_company.html'

class CreateUser(CustomHtmxMixin, TemplateView):
    template_name = 'create_user.html'

class Login(TemplateView):
    template_name = 'login.html'

class Main(CustomHtmxMixin, TemplateView):
    template_name = 'main.html'

class Users(CustomHtmxMixin, TemplateView):
    template_name = 'users.html'


