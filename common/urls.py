from django.urls import path
from . import views
app_name='common'
urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.home, name='home'),
    path('customerLogin',views.customerLogin, name='customerLogin'),
    path('customerReg',views.customerReg, name='customerReg'),
    path('sellerLogin',views.sellerLogin, name='sellerLogin'),
    path('sellerReg',views.sellerReg, name='sellerReg'),
]