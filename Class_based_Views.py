Here insted of using functions we use classes and we use the APIVies. Then in the urls folder we have to do this 

urlpatterns = [
    path('products/',views.ProductList.as_view()),
    path('product-details/<int:id>',views.Product_details.as_view())
]




This is our vies file



from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer




class ProductList(APIView):
      def get (self,request):
           queryset = Product.objects.select_related('collection')
           serializer = ProductSerializer(queryset, many =True)
           return Response(serializer.data)
      def post(self,request):
           serializer = ProductSerializer(data = request.data)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           print(serializer.data)
           return Response(serializer.data)
              

# @api_view(['POST'])
# def product_list(request):
#     if request.method == 'GET':
#        queryset = Product.objects.select_related('collection')
#        serializer = ProductSerializer(queryset, many =True)
       
#        return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer.data)
#         return Response(serializer.data)
    
        
    

class Product_details(APIView):
      

      def get(self,request,id):
        product = get_object_or_404(Product,pk =id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
      def put(self,request,id):
        product = get_object_or_404(Product,pk =id)
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
      def delete(self,request,id):
          product = get_object_or_404(Product,pk =id)
          product.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

             
































































































































































....
