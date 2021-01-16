from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self, request):
        products = None
        category = Category.get_all_category()

        categoryid = request.GET.get('category')

        if categoryid:
            products = Product.get_all_products_by_categoryid(categoryid)
        else:
            products = Product.get_all_products()

        context = {
            'products': products,
            'category': category
        }

        print('email', request.session.get('customer_email'))
        return render(request, 'store/index.html', context)

    def post(self, request):
        product = request.POST.get('product')
        print(product)

        return redirect('store:index')
