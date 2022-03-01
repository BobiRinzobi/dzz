from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from django.core.paginator import Paginator

from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm


class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context



class ProductDetailView(DetailView):
    template_name = 'sample_app/product_detail.html'
    queryset = Product.objects.all()



class ProductCreateView(CreateView):
    template_name = 'sample_app/product_create.html'
    form_class = ProductForm

class ProductUpdateView(UpdateView):
    template_name = 'sample_app/product_create.html'
    form_class = ProductForm


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)



class ProductDeleteView(DeleteView):
    template_name = 'sample_app/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'
