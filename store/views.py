from django.shortcuts import get_object_or_404
from store.forms import ProductFilterForm
from store.models import Product, Category
from django.views.generic import TemplateView, ListView, DetailView


class HomeView(TemplateView):
    template_name = 'home.html'


class CategoryListView(ListView):
    model = Product
    template_name = 'category_list.html'
    form_class = ProductFilterForm
    paginate_by = 5
    context_object_name = 'object_list'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            products = get_products_for_category(category)
        else:
            products = Product.objects.all()

        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('q')
            if query:
                products = products.filter(name__icontains=query.strip())

            price = form.cleaned_data.get('price')
            if price:
                products = products.filter(price__lte=price)

        discount_filter = self.request.GET.get('discount_filter')
        if discount_filter == 'discounted':
            products = products.filter(discount_percentage__gt=0)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')

        parent_categories = Category.objects.filter(parent__isnull=True)
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            subcategories = category.sub_categories.all()
            context['category'] = category
        else:
            subcategories = parent_categories

        category_data = [
            {
                'cat': cat,
                'product_count': get_products_for_category(cat).count()
            }
            for cat in subcategories
        ]
        context.update({
            'category_data': category_data,
            'parent_categories': parent_categories,
            'form': self.form_class(self.request.GET),
        })
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        category = product.categories.get()
        product_count = get_products_for_category(category).count()

        context['product_count'] = product_count
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


def get_all_categories(category):
    all_category = [category]
    for sub_category in category.sub_categories.all():
        all_category.extend(get_all_categories(sub_category))

    return all_category


def get_products_for_category(category):
    all_category = get_all_categories(category)

    return Product.objects.filter(categories__in=all_category).distinct()
