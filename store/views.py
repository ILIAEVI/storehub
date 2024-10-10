from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.forms import ProductForm
from store.models import Product, Category


@login_required()
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    product_data = []

    for product in products:
        product_data.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'image': product.image.url if product.image else None,
            'categories': [
                {
                'id': category.id,
                'name': category.name,
                'parent_id': category.parent_id,
                }
                for category in product.categories.all()
            ]
        })

    return JsonResponse(product_data, safe=False)


def category_list(request):
    root_categories = Category.objects.filter(parent__isnull=True)

    def get_sub_categories(category):
        return {
            'id': category.id,
            'name': category.name,
            'sub_categories': [get_sub_categories(sub_cat) for sub_cat in category.sub_categories.all()]
        }

    data = [get_sub_categories(cat) for cat in root_categories]

    return JsonResponse(data, safe=False)
