# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer


# class ProductList(APIView):
#     def get(self, request):
#         prod = Product.objects.all()[:20]
#         data = ProductSerializer(prod, many=True).data
#         return Response(data)
#
#
# class ProductDetail(APIView):
#     def get(self, request, pk):
#         prod = get_object_or_404(Product, pk=pk)
#         data = ProductSerializer(prod).data
#         return Response(data)

# ListCreateAPIView allow Post and Get sentences
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# RetriveDestroyAPIView allow Get/:id and Delete Sentences
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class SubCategoryList(generics.ListCreateAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer


# RetriveUpdateDestroyAPIView allow use patch and pu
# createAPiView just allow Post access
class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategory.objects.filter(category_id=self.kwargs["pk"])
        return queryset

    serializer_class = SubCategorySerializer
