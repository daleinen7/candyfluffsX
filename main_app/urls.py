from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('conventions/', views.conventions, name='conventions'), 
    path('products', views.ProductsList.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]