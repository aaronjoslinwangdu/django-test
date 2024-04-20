from django.shortcuts import render
from django.views.generic import ListView
from .models import Cat

# Create your views here.

class AllCats(ListView):
    model = Cat
    template_name = "cats/index.html"

class YvonneCats(ListView):
    model = Cat
    template_name = "cats/yvonne.html"

    def get_queryset(self):
        return Cat.objects.filter(weight__lte=10)


