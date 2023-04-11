from django.urls import path
from . import views
app_name='seller'
urlpatterns = [
    
    path('s_home',views.s_home,name='s_home'),
    path('product_catalogue',views.product_catalogue,name='product_catalogue'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('update_products',views.update_products,name='update_products'),
    path('update_stock',views.update_stock,name='update_stock'),
    path('delete_product/<int:p_id>',views.delete_product,name='delete_product'),
    path('product_view/<int:p_id>',views.product_view,name='product_view'),
    path('index',views.index,name='index'),
    path('number',views.number,name='number'),
]