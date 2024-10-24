from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from store.forms import ProductFilterForm
from store.models import Product, Category


def home(request):
    return render(request, 'home.html')


def categories(request, category_id=None):
    parent_categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.all()

    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        subcategories = category.sub_categories.all()
        products = get_products_for_category(category)
    else:
        category = None
        subcategories = parent_categories

    form = ProductFilterForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('q')
        if query:
            query = query.strip()
            products = products.filter(name__icontains=query)

        price = form.cleaned_data.get('price')
        if price:
            products = products.filter(price__lte=price)

    discount_filter = request.GET.get('discount_filter')
    if discount_filter == 'discounted':
        products = products.filter(discount_percentage__gt=0)

    category_data = []
    for cat in subcategories:
        product_count = get_products_for_category(cat).count()
        category_data.append({
            'cat': cat,
            'product_count': product_count,
        })

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category_data': category_data,
        'category': category,
        'parent_categories': parent_categories,
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'category_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    category = product.categories.get()

    product_count = get_products_for_category(category).count()
    context = {'product': product, 'product_count': product_count}

    return render(request, 'product_detail.html', context)


def contact(request):
    return render(request, 'contact.html')


def get_all_categories(category):
    all_category = [category]
    for sub_category in category.sub_categories.all():
        all_category.extend(get_all_categories(sub_category))

    return all_category


def get_products_for_category(category):
    all_category = get_all_categories(category)

    return Product.objects.filter(categories__in=all_category).distinct()
