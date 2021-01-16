from django.views import View
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import Product
from.models.category import Category
from.models.customer import Customer

# Create your views here.
# index


def index(request):
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
    return render(request, 'store/index.html', context)

# Signup


class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        return self.registerUser(request)

    def registerUser(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)

        error_message = self.validateCustomer(customer)

        if not error_message:

            customer.password = make_password(customer.password)

            customer.register()

            return redirect('store:index')

        else:

            context = {'error': error_message, 'values': value}

            return render(request, 'store/signup.html', context)

    def validateCustomer(self, customer):

        error_message = None

        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 3:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 3:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'

        elif customer.isExists():
            error_message = 'Email already exists'

        return error_message


# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'store/signup.html')
#     else:
#         return registerUser(request)


# def registerUser(request):
#     first_name = request.POST.get('firstname')
#     last_name = request.POST.get('lastname')
#     phone = request.POST.get('phone')
#     email = request.POST.get('email')
#     password = request.POST.get('password')

#     # validation
#     value = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone': phone,
#         'email': email
#     }

#     error_message = None

#     customer = Customer(first_name=first_name, last_name=last_name,
#                         phone=phone, email=email, password=password)

#     error_message = validateCustomer(customer)

#     if not error_message:

#         customer.password = make_password(customer.password)

#         customer.register()

#         return redirect('store:index')

#     else:

#         context = {'error': error_message, 'values': value}

#         return render(request, 'store/signup.html', context)


# def validateCustomer(customer):

#     error_message = None

#     if (not customer.first_name):
#         error_message = "First Name Required !!"
#     elif len(customer.first_name) < 3:
#         error_message = 'First Name must be 4 char long or more'
#     elif not customer.last_name:
#         error_message = 'Last Name Required'
#     elif len(customer.last_name) < 3:
#         error_message = 'Last Name must be 4 char long or more'
#     elif not customer.phone:
#         error_message = 'Phone Number required'
#     elif len(customer.phone) < 10:
#         error_message = 'Phone Number must be 10 char Long'
#     elif len(customer.password) < 6:
#         error_message = 'Password must be 6 char long'
#     elif len(customer.email) < 5:
#         error_message = 'Email must be 5 char long'

#     elif customer.isExists():
#         error_message = 'Email already exists'

#     return error_message


# LOgin

class Login(View):

    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('store:index')
            else:
                error_message = 'Email or password Envalid'
        else:
            error_message = 'Email or Password Envalid'

        return render(request, 'store/login.html', {'error': error_message})


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'store/login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)

#         error_message = None

#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('store:index')
#             else:
#                 error_message = 'Email or password Envalid'
#         else:
#             error_message = 'Email or Password Envalid'

#         return render(request, 'store/login.html', {'error': error_message})
