from django.urls import path
from . import views
app_name='customer'
urlpatterns = [
    # path('',views.index,name='index'),
    path('c_home',views.c_home, name='c_home'),
]