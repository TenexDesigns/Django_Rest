



This is creating serializers. wecrate this in a file called serializers.py


from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length =255)
    unit_price = serializers.DecimalField(max_digits=6,decimal_places=2)















This is what we do in the views file . This is serializing the objects


from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer



@api_view()
def product_details(request,id):
    try:
        product  = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    except Product.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND)    
    




We can also insted the get_object_or_404 method insted of the try and except method.


from django.shortcuts import render,get_object_or_404  // We use this insetad of the try and except block.
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer




@api_view()
def product_details(request,id):
    product = get_object_or_404(Product,pk =id)

    serializer = ProductSerializer(product)
    return Response(serializer.data)




  
  WE CAN ASLO GET ALL PRODUCTS FROM THE DATABASE


  
  from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many =True)  // Here we put the many option because we want to infor the serialavzer
                                                           method that the objects are many that are beng passed and not one

    return Response(serializer.data)






























































































...
