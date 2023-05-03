Model Serilaizer


This help us avoid repeadting ourselves.
Do you seee all of the commented out code, all of that is replaced with the two lines of code     class Meta:
                                                                                                         model = Product
                                                                                                         fields = ['id','unit_price','collection']

This heps us avoid repetition and reduces the amount of code
      
      
from decimal import Decimal
from rest_framework import serializers

from store.models import Product,Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','unit_price','collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length =255)
    # #we can also rename our fields, e.g Here we rename unit_price in produsts to price, SInce django assumes unit_price
    #is in products, it will also assume that the renamed field of price is also in the produts, but price is not there,
    #so we have to give the source of this renamed field as 'unit_price' from the product
    # price = serializers.DecimalField(max_digits=6,decimal_places=2,source ='unit_price')
    # #unit_price = serializers.DecimalField(max_digits=6,decimal_places=2)
    # #This is the new custom field  tht is presneted at this end point. It is calculated through the specifie method here below.
    # price_with_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all()
    # )
    
        # def calculate_tax(self,product:Product):
    #     return product.unit_price * Decimal(1.1)









INCASE WE WANT TO ADD A COMPUTED FIELD 


from decimal import Decimal
from rest_framework import serializers

from store.models import Product,Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','unit_price','calculate_tax','collection']
        
     price_with_tax = serializers.SerializerMethodField(method_name= 'calculate_tax')
   

  
       def calculate_tax(self,product:Product):
           return product.unit_price * Decimal(1.1)





HERE WE CAN ALSO RENAME A  FILED





from decimal import Decimal
from rest_framework import serializers

from store.models import Product,Collection

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','price','collection']
        
     price = serializers.DecimalField(max_digits=6,decimal_places=2,source ='unit_price')
    
   

  
       def calculate_tax(self,product:Product):
           return product.unit_price * Decimal(1.1)






HERE IS MORE EXPLANATION
******************************************************************************************************************************************************************



In Django Rest Framework (DRF), model serializers are used to serialize and deserialize Django models. 
They are similar to regular Django form classes, but are optimized for use with APIs.

To use a model serializer in DRF, you need to define a serializer class that inherits from DRF's serializers.ModelSerializer.
Heres an example serializer for a Book mode



from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description']





In this example, the BookSerializer class defines a Meta class that specifies the Book model as the model to be serialized, and a list of fields 
to include in the serialized output.

To use this serializer in a view, you would first retrieve the Book objects you want to serialize, and then pass them to the serializer class:



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)





In this example, the BookList view retrieves all Book objects and passes them to the BookSerializer class with the many=True argument,
indicating that there may be multiple objects to serialize.

The serializer.data attribute contains the serialized data in a Python dictionary format, which is then returned in the API response.

Overall, model serializers in DRF provide an easy and efficient way to serialize and deserialize Django models for use in APIs.







HERE IS MORE EXPLANATION
************************************************************************************************************************************************************


Model serializers in Django REST framework provide a convenient way to convert Django models into JSON or other content types. 
They are a layer of abstraction over the default serializer and help in quickly creating serializers for Django models.
There are two major serializers used in Django REST framework: ModelSerializer and HyperlinkedModelSerializer



Using ModelSerializers

ModelSerializers are similar to Django ModelForm classes.
They automatically generate a set of fields and default validation based on the underlying model class.
Heres an example of using ModelSerializer for a Snippet model:


  
  from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']



Using different serializers in the same ModelViewSet

In some cases, you might want to use different serializers for different actions in a ModelViewSet.
You can achieve this by overriding the get_serializer_class method in your ModelViewSet. Here's an example:



from rest_framework import viewsets
from .serializers import ListaGruppi, DettaglioGruppi, Default

class DualSerializerViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return ListaGruppi
        if self.action == 'retrieve':
            return DettaglioGruppi
        return Default





Creating a viewset

To render data into the frontend and handle user requests, you need to create a view.
In Django REST framework, views are called viewsets. Heres an example of creating a viewset for a GeeksModel:


from rest_framework import viewsets
from .serializers import GeeksSerializer
from .models import GeeksModel

class GeeksViewSet(viewsets.ModelViewSet):
    queryset = GeeksModel.objects.all()
    serializer_class = GeeksSerializer




HyperlinkedModelSerializer

HyperlinkedModelSerializer works similarly to ModelSerializer but uses hyperlinked relationships instead of primary key relationships. 
Heres an example of using HyperlinkedModelSerializer for an Account model:


from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']



In summary, model serializers in Django REST framework help you easily convert Django models to JSON or other content types, 
and create viewsets for handling user requests. You can use ModelSerializer or HyperlinkedModelSerializer depending on your needs,
and even use different serializers for different actions in a ModelViewSet.




































































































...
