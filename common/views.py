from django.shortcuts import redirect, render
from django.http import HttpResponse

from common.models import Customer, Seller

# Create your views here.

# def index(request):
    # return HttpResponse('''congratulations you have created a web application ''')

def home(request):
    return render(request, 'home.html')

def customerLogin(request):
    msg = ''
    if request.method == 'POST':
        c_username = request.POST['username']
        c_password = request.POST['password']

        try:
            customer = Customer.objects.get(
                c_email = c_username,
                c_password = c_password 
            )
            request.session['customer'] = customer.id
            return redirect('customer:c_home')
        except:
            msg = 'invalid username or password',{'message:msg'}


    return render(request, 'customerLogin.html')

def customerReg(request):
    msg = ''
    if request.method == 'POST' :
        customer_name = request.POST['cname']
        customer_email = request.POST['cemail']
        customer_mobile = request.POST['cmobile']
        customer_password = request.POST['cpassword']

        try:
            new_customer = Customer(
                c_name = customer_name,
                c_email = customer_email,
                c_mobile = customer_mobile,
                c_password = customer_password
            )
            new_customer.save()
            msg ='Succesfully Registered'
        except:
            msg = 'Invalid Data'

    return render(request, 'customerReg.html', {'message':msg})

def sellerLogin(request):
    msg = ''
    if request.method == 'POST':
        s_username = request.POST['username']
        s_password = request.POST['password']

        try:
            seller = Seller.objects.get(
            s_email = s_username,
            s_password = s_password
            )
            request.session['seller']=seller.id
            return redirect('seller:s_home')
        except:
            msg = 'invalid username or password',{'message:msg'}

    return render(request, 'sellerLogin.html')

def sellerReg(request):
    msg = ''
    if request.method == 'POST' :
        seller_name = request.POST['sname']
        seller_email = request.POST['semail']
        seller_mobile = request.POST['smobile']
        seller_password = request.POST['spassword']

        try:
            new_seller = Seller(
                s_name = seller_name,
                s_email = seller_email,
                s_mobile = seller_mobile,
                s_password = seller_password
            )
            new_seller.save()
            msg = 'Succesfully Registered'
        except:
            msg = 'Invalid Data'

    return render(request, 'sellerReg.html',{'message':msg})
