Desierialization is whne we receive data from the user to the database
THis is possible throught the post method.
In this here below method, we use if else block to try and see which method is being accesed.
If it is get, we serialize the data , if it is post , we desierialize the data

























from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
       queryset = Product.objects.select_related('collection')
       serializer = ProductSerializer(queryset, many =True)

       return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        # The data will be available at serializer.validata_data
        # Here we check if the data returned is valid or not.
        if serializer.is_valid():
            serializer.validated_data
            return Response('That is the correct answer')
        else:

            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)






We can also write the last part of this code in simpler lines like this 


from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
       queryset = Product.objects.select_related('collection')
       serializer = ProductSerializer(queryset, many =True)

       return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        # The data will be available at serializer.validata_data
        serializer.is_valid(raise_exception =True):
        serializer.validated_data
        Response('That is the correct answer')
        





SAVING A PRODUCT



from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
       queryset = Product.objects.select_related('collection')
       serializer = ProductSerializer(queryset, many =True)

       return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        # The data will be available at serializer.validata_data
        serializer.is_valid(raise_exception =True):
        serializer.save()
     
        Response('That is the correct answer')







Updating an object


@api_view(['GET','PUT'])
def product_details(request,id):
    product = get_object_or_404(Product,pk =id)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




Deleteing an object





@api_view(['GET','PUT','DELETE'])
def product_details(request,id):
    product = get_object_or_404(Product,pk =id)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method =='DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)













































































































...
