from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class homepageview(TemplateView):
    template_name = 'home.html'

class contactspageview(TemplateView):
    template_name = 'contacts.html'

class shoespageview(TemplateView):
    template_name = 'shoes.html'