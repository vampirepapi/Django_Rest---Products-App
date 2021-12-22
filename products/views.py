# from django.shortcuts import render
from django.shortcuts import get_object_or_404
# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductItemSerializer
from .models import ProductItem

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from rest_framework import generics

class ProductItemViews(APIView):
    def post(self, request):
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request, id=None):
        if id:
            item = ProductItem.objects.get(id=id)
            serializer = ProductItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ProductItem.objects.all()
        serializer = ProductItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


    def patch(self, request, id=None):
        item = ProductItem.objects.get(id=id)
        serializer = ProductItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, id=None):
        item = get_object_or_404(ProductItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})



    # def get(self, request, price=None):
    #     if id:
    #         item = ProductItem.objects.get(price=price)
    #         serializer = ProductItemSerializer(item)
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

# class ProductItemViews(APIView):
#     queryset = ProductItem.objects.all()
#     serializer_class = ProductItemSerializer
#     # permission_classes = [IsOwner]
#     filterset_fields = ('product_price', ) 
class ProductItemViews(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    name = 'product-list'
    
    filter_fields = (
        'product_price',
        'product_quantity',
    )
