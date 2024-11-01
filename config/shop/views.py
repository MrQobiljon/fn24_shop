from django.shortcuts import render
from django.views.generic import View

from .models import Category, Product, Images

# Create your views here.


class Index(View):
    def get(self, request, pk=None):
        products = Product.objects.all()
        categories = Category.objects.filter(parent=None)
        context = {
            "products": products,
            "categories": categories
        }
        return render(request, "index.html", context)