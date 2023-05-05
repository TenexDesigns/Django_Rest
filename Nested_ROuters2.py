
1.THE MODELS AND THEIR RELATIONSHIP



THIS IS THE COLLECTION CLASS MODEL, IT IS GOING TO BE THE PARRENT OF THE PRODUCTS CLASS.
tHERE ARE EIGHT COLLECTIONS AND ALL 100 PRODUCT CAN BE IN ONE OF THIS COLLECTIONS
THERE IS A ONE TO MANY RELATIONSHIP BETWEEN THE COLLECTIONS AND THE PRODUCTS CLASS
# class Collection(models.Model):
#     title = models.CharField(max_length=255)
#     featured_product = models.ForeignKey(
#         'Product', on_delete=models.SET_NULL, null=True, related_name='+', blank=True)

#     def __str__(self) -> str:
#         return self.title

#     class Meta:
#         ordering = ['title']



THIS IS THE PRODUCT CLASS MODEL, IT IS THE CHILD OF THE COLLECTION CLASS
# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField()
#     description = models.TextField(null=True, blank=True)
#     unit_price = models.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         validators=[MinValueValidator(1)])
#     inventory = models.IntegerField(validators=[MinValueValidator(0)])
#     last_update = models.DateTimeField(auto_now=True)
#     collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
#     promotions = models.ManyToManyField(Promotion, blank=True)











2. SERIALIZATION

Here we serialize the data, i.e convert the data into json so that it can be read by the broser
We use the ModelSerializer and give the fields from our model that we want to be displayed.


from rest_framework import serializers
from store.models import Product,Collection,



class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id','title',]






class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','unit_price','inventory','collection']
    














3.THE VIEW 

These views are used to handle the reuest from our browsers
Here we are going to use the Model View set to handle this requests
The collection list handles the collection data and returns a list of all collections
The Productlist handles the products data and retunrs the products data



class CollectionList(ModelViewSet):
      queryset =    Collection.objects.all()
      serializer_class = CollectionSerializer





class ProductList(ModelViewSet):
      serializer_class = ProductSerializer
      

      def get_queryset(self):
           return Product.objects.filter(collection_id = self.kwargs['collection_pk'])
        
        
  // Here we are filtering the products retuned to be in the collection given in the url
 //  We get the colllection from id from the url like here below  



     # self.kwargs - This is a dictionary that contains our url parameters
      #Remember that our url has two paramters, collection_pk and pk






4. THE URLS FILE

This is where we  nest our routers,
So to get the complete url 
http://127.0.0.1:8000/store/collections                    - Lists all 8 colllections
http://127.0.0.1:8000/store/collections/4/                 - List only the fourth collection
http://127.0.0.1:8000/store/collections/4/products         - List all products in the fourth collection
http://127.0.0.1:8000/store/collections/4/products/288/    - This lits product of id 288 which is of colletion 4


from django.urls import include, path
from rest_framework_nested import routers
from .views import ProductList,CollectionList

router = routers.DefaultRouter()
router.register(r'collections', CollectionList)
# Here we create a router like normal

# Then this si where the nesting happens, First we create the  NestedDraultRouter and pass to it the oarent router and the doman of the orent router
# We also passs a lookup, that will be used as a orifix for te look up paremeter i.e /collection/{collection_id/product/{pk}}
#Remember that our url has two paramters, collection_pkk and pk
products_router =  routers.NestedDefaultRouter(router,'collections',lookup ='collection')
products_router.register('products',ProductList,basename='collection-products')
# Above here we regester the nested router or child router , give it it;s prefix which is products, give it its view set and the base name 
# The base name will be used for generating the name of our url patterns
# When we use a router to regester a route, that router generats two url patterns, one is called list, the other is called detail, so the value in the base name will be used as a prefix of the list and detail views




#urlpatterns = router.urls + products_router.urls

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'',include(products_router.urls))
]


























































































































































































































































































...
