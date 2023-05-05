WE CAN USE THIS TO FILTER ITEMS FROM THE URL


THERE IS  TWO WAYS TO DO THIS, THER IS THE MANUAL WAY WHERE WE DECLARE THE CLASS TO BE USED TO FILTER , AND THEN THER IS USING THE DJANGO-FILTER PACKAGE 
http://127.0.0.1:8000/store/products/
http://127.0.0.1:8000/store/products/?collection_id=1
http://127.0.0.1:8000/store/products/?collection_id=2
http://127.0.0.1:8000/store/products/?collection_id=3




    
    
    
    THIS IS THE MANUAL WAY
*********************************************************************************************8

THERE ARE TWO MODEL CLASSES

ONE IS PRODUCT MODEL CLASS WITH 1000 OBJECTS AND THE OTHER IS COLLLECTION CLASS 1ITH 8 OPTIONS
ALL THE ONETHOUSAND PRODUCT HAVE TO BE IN ONE OF THESE COLLECTIONS
SO THERE IS A ONE TO MANY RELATIONHIP BETWEEN THE PRODUCTS AND COLLECTION CLASSES


tHE PROCUTS END POINT LUISTS ALL PRODYTS , IRREGRADLESS OF THEIR COLLECTION
WHEN WE ADD A COLLECTION ID TO THE URL, , WE USE THAT ID TO FILTER ONLY THE PRODUCTS BELONGING TO THAT COLLECTION ID
let us seee how to grab this collection id from the url



http://127.0.0.1:8000/store/products/
http://127.0.0.1:8000/store/products/?collection_id=1
http://127.0.0.1:8000/store/products/?collection_id=2
http://127.0.0.1:8000/store/products/?collection_id=3




let us seee how to grab this collection id from the url



class ProductList(ModelViewSet):
      serializer_class = ProductSerializer
      

      def get_queryset(self):
            collection_id =self.request.query_params.get('collection_id')  // This is how we get the collection id
            queryset = Product.objects.all()
            if collection_id is not None:
                 queryset2 = queryset.filter(collection_id=collection_id)  // Here we filter  the returned objects based on the collection id
                 return queryset2
            else:
                 return queryset   //if there is no collection id in the url , we return the original query set













THIS IS THE WAY USING THE DJANGO-FILTER PACKAGE
*****************************************************************************************************************************************************

from django_filters.rest_framework import DjangoFilterBackend,FilterSet,filterset
from .models import Product
from rest_framework.viewsets import ModelViewSet


class ProductList(ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      filter_backends = [DjangoFilterBackend]  // THI SIS WHAT WE IMPORTED AND MUST BE DECLARED
      filterset_fields = ['collection_id']           //HERE WE JUST DECLARE THE FIELD TO BE USED FOR FILTER











HOWEVER IF WE WANT TO PUT CUSTOM MODIFICATIONS, LIKE BEING ABLE TO FILTER THE PRODUCTS BASED ON THEIR COLLECTIO ID AND THEN ON THEIR UNIT PRICE
*****************************************************************************************************************************************************
WE NEED TO CREATE A FILE IN THE APP AND NAME IT FILTER
IN THAT FILE WE CREATE A FILE AND NAME IT PRODUCTFILTER, AND WE PUT IN IT THE THINGS WE WANT TO BE ABLE TO FILTER BY



from django_filters.rest_framework import DjangoFilterBackend,FilterSet,filterset
from .models import Product



class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id':['exact'],
            'unit_price':['gt','lt']
        }






THEN IN UR VIEWS FILE WE INCLUDE THAT FILE IN OUR FILTERSET_FIELDS



class ProductList(ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      filter_backends = [DjangoFilterBackend]
      filterset_class = ProductFilter



      
      This can even give us a url like this
      http://127.0.0.1:8000/store/products/?collection_id=6&unit_price__gt=60&unit_price__lt=90

































...
