"""djangorest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .apiviews import ProductList, ProductDetail, CategoryList, CategoryDetail, SubCategoryList, SubCategoryDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    # get all products
    path('api/v1/products/', ProductList.as_view(), name='products_list'),
    # get only one product
    path('api/v1/products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    # get all categories
    path('api/v1/categories/', CategoryList.as_view(), name='categories_list'),
    #get category by id
    path('api/v1/categories/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    # get subcategories by id
    path('api/v1/subcategories/<int:pk>', SubCategoryDetail.as_view(), name='subcategory_detail'),
    # get relational cateogories by subcategories
    path('api/v1/categories/<int:pk>/subcategories/', SubCategoryList.as_view(), name='category_list')
    # here we need add more endpoints 

]

















