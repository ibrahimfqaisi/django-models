from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"
    
class SnackDetailView(ListView):
    model = Snack
    template_name = "snack_detail.html"
