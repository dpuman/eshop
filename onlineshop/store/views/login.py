from django.views import View
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from store.models.customer import Customer


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
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('store:index')
            else:
                error_message = 'Email or password Envalid'
        else:
            error_message = 'Email or Password Envalid'

        return render(request, 'store/login.html', {'error': error_message})
