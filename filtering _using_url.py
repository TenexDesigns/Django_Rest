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





THEN IN OUR URLS.PY FILE




from rest_framework_nested import routers
from .views import ProductList,CollectionList,ProductViewSet

router = routers.DefaultRouter()
router.register(r'products',ProductList,basename='product' )






THIS IS OUR SERILAIZER


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','unit_price','inventory','collection']
    










































































































...
