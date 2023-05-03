Desierialization is whne we receive data from the user to the database
THis is possible throught the post method.
In this here below method, we use if else block to try and see which method is being accesed.
If it is get, we serialize the data , if it is post , we desierialize the data



Deserialization is the process of converting structured data (e.g. JSON, XML) into Python objects. 
In Django Rest Framework (DRF), deserialization is typically done using serializers. Here are some common operations related to deserialization in DRF:

Data Validation:
When deserializing data, its important to ensure that the data is valid. DRF serializers provide a variety of built-in validators that can be 
used to enforce data validation rules. These validators include things like validating field types, checking field lengths,
and verifying uniqueness constraints.

Saving Objects:
After deserializing data, you typically want to save the data as a new object in your database.
To do this, you can use the serializer create method. This method takes the deserialized data and creates a new object instance in the database.

Updating Objects:
If you want to update an existing object in the database, you can use the serializers update method.
This method takes an existing object instance and the deserialized data, and updates the object with the new data.

Deleting Objects:
To delete an object from the database, you can use the delete method on the object instance.

Overall, DRF serializers provide a powerful and flexible way to handle deserialization and data validation in your Django projects.






















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
