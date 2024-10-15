from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
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
                    'parent': {
                        'id': category.parent.id,
                        'name': category.parent.name
                    } if category.parent else None
                }
                for category in product.categories.all()
            ]
        })

    return JsonResponse(product_data, safe=False)


def get_all_categories(category):
    categories = [category]
    for sub_category in category.sub_categories.all():
        categories.extend(get_all_categories(sub_category))

    return categories


def get_products_for_category(category):
    categories = get_all_categories(category)

    return Product.objects.filter(categories__in=categories).distinct()


def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)

    category_data = []
    for category in categories:
        product_count = get_products_for_category(category).count()
        category_data.append({
            'category': category,
            'product_count': product_count,
        })

    context = {
        'category_data': category_data,
    }
    return render(request, 'category_list.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(categories__in=get_all_categories(category)).distinct()

    product_details = [
        {
            'product': product,
            'total_cost': product.price * product.quantity
        }
        for product in products
    ]

    paginator = Paginator(product_details, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if products.exists():
        most_expensive_product = products.order_by('-price').first()
        cheapest_product = products.order_by('price').first()
        average_price = products.aggregate(Avg('price'))['price__avg']
        total_value = products.aggregate(Sum('price'))['price__sum'] * sum(product.quantity for product in products)

        statistics = {
            'most_expensive_product': most_expensive_product,
            'cheapest_product': cheapest_product,
            'average_price': average_price,
            'total_value': total_value,
        }
    else:
        statistics = {
            'most_expensive_product': None,
            'cheapest_product': None,
            'average_price': 0,
            'total_value': 0,
        }

    context = {
        'category': category,
        'page_obj': page_obj,
        'statistics': statistics,
    }

    return render(request, 'category_detail.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)
