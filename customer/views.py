from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('this is customer module')
def c_home(request):
    
    return render(request, 'c_home.html')
