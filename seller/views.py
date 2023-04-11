from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from seller.models import AddProducts

# Create your views here.

# def index(request):
#     return HttpResponse('this is customer module')
def s_home(request):
    return render(request, 's_home.html')

def product_catalogue(request):
    msg =''

    if request.method == 'POST' :
        seller_category = request.POST['s_category']
        seller_productname = request.POST['s_product_name']
        seller_description = request.POST['s_description']
        seller_productstock = request.POST['s_product_stock']
        seller_productprice = request.POST['s_product_price']
        seller_productimage = request.FILES['image1']

        try:
            new_product = AddProducts(
                category = seller_category,
                product_name = seller_productname,
                description = seller_description,
                product_stock = seller_productstock,
                product_price = seller_productprice,
                seller_id=request.session['seller'],
                image = seller_productimage
            )
            new_product.save()
            msg = 'Success'
        except:
            msg = 'Invalid Data'

    return render(request, 'product_catalogue.html')

def viewproduct(request):
    products = AddProducts.objects.filter(seller_id= request.session['seller'])
    return render(request, 'viewproduct.html',{'products':products})

def update_products(request):
    msg=''
    products = AddProducts.objects.filter(seller_id= request.session['seller'])
    if request.method == 'POST':
        # seller_category = request.POST['']
        pid = request.POST['product']
        print(pid)
        seller_productname = request.POST['s_product_name']
        seller_description = request.POST['s_description']
        seller_productstock = request.POST['s_product_stock']
        seller_productprice = request.POST['s_product_price']

        product = AddProducts.objects.get(id=pid)
        
        product.product_name = seller_productname
        product.description = seller_description
        product.product_stock = seller_productstock
        product.product_price = seller_productprice
        product.save()
        msg='update succesfull'
        

    return render(request, 'update_products.html',{'products':products,'message':msg})

def update_stock(request):
    p_id = request.POST['id']
    product = AddProducts.objects.get(id=p_id)
    data = [{'category':product.category,'product_name':product.product_name,'description':product.description,'product_stock':product.product_stock,'product_price':product.product_price}]
    return JsonResponse({'data':data})

def delete_product(request,p_id):
    product = AddProducts.objects.get(id = p_id)
    product.delete()
    msg = 'Delete succesfully'
    products = AddProducts.objects.filter(seller_id= request.session['seller'])
    return render(request, 'viewproduct.html',{'products':products,'message':msg})

def product_view(request,p_id):
    product = AddProducts.objects.get(id = p_id)
    return render(request, 'product_view.html',{'products':product})

@api_view(['GET'])
def index(request):
    message = 'Congratulations...you have created an API'
    return Response(message)

@api_view(['GET'])
def number(request):
    message = 10
    return Response(message)
