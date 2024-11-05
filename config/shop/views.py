from django.shortcuts import render, redirect
from django.views.generic import (View, ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.db.models import Q

from .models import Category, Product, Images, Review

# Create your views here.


class Index(View):
    def get(self, request, pk=None):
        products = Product.objects.all()
        categories = Category.objects.filter(parent=None)
        reviews = Review.objects.all()
        context = {
            "products": products,
            "categories": categories,
            'organic_products': products.filter(quality='or'),
            'reviews': reviews
        }
        return render(request, "index.html", context)

    def post(self, request):
        try:
            full_name = request.POST["full_name"]
            profession = request.POST['profession']
            text = request.POST['text']
            rate = request.POST['rate']

            if full_name and profession and text and rate:
                print("test ------------------------------")
                if request.user.is_authenticated:
                    review = Review.objects.create(
                        text=text,
                        user=request.user,
                        full_name=full_name,
                        profession=profession,
                        rating=int(rate)
                    )
                return redirect('home')
        except:
            pass
        return redirect('home')


class ShopView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = "products"
    extra_context = {
        "title": "Barcha mahsulotlar",
        "subcategories": Category.objects.exclude(parent=None)
    }


class ProductByCategory(ShopView):
    def get_queryset(self):
        word = self.request.GET.get("q")
        if word:
            return Product.objects.filter(Q(name__icontains=word) | Q(description__icontains=word))
        return Product.objects.filter(category__slug=self.kwargs.get("slug"))