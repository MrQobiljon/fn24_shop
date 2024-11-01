from django.template import Library
from ..models import Category, Product

register = Library()


@register.simple_tag()
def get_products_by_category(category_id = None):
    if not category_id:
        products = Product.objects.all()[:8]
    else:
        category = Category.objects.get(pk=category_id)
        # subcategories = Category.objects.filter(parent=category)
        subcategories = category.subcategories.all()
        products = []
        for subcategory in subcategories:
            for product in subcategory.products.all():
                if len(products) >= 8:
                    break
                products.append(product)

            if len(products) >= 8:
                break
    return products