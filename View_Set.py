
The model view set is used to help prevent code repetion



For example , We use this to read,update and delete data,

class Product_details(RetrieveUpdateDestroyAPIView):
      queryset =  Product.objects.all()
      serializer_class = ProductSerializer

      
      We also use this to list the data


class Product_details(ListCreateAPIView):
      queryset =  Product.objects.all()
      serializer_class = ProductSerializer




But as you can see here, There is a alot of code repetion 

This is where view sets come in and help us prevent this code repetion and combine similar code
.
This handles both thee classes above.
However , if you onl want this to display data only  and not to write, you can use the ReadOnlyModelViewSet

from rest_framework.viewsets import ModelViewSet


      class ProductViewSet(ModelViewSet):
          queryset =  Product.objects.all()
          serializer_class = ProductSerializer


e.g




HERE IS ANOTHER EXAMPLE

For  example this is used to retrive, update and delete data.

class Product_details(RetrieveUpdateDestroyAPIView):
      queryset =  Product.objects.all()
      serializer_class = ProductSerializer
      lookup_field = 'id'

      def delete(self, request,id):
           product = get_object_or_404(Product,pkid)
           if product.id > 40 :
                return Response({'error':'Product Can not be deleted, it is above 49, have mercy'})
           product.delete()

           return Response(status= status.HTTP_204_NO_CONTENT) 


This is used to get  data




class Product_details(RetrieveUpdateDestroyAPIView):
      queryset =  Product.objects.all()
      serializer_class = ProductSerializer




      
      We can combine bot of them to give us this one class that performs all of this functionality using the  view set 



      class ProductViewSet(ModelViewSet):
      def get_queryset(self):
          return Product.objects.all()
      def get_serializer_class(self):
          return ProductSerializer
      
      lookup_field = 'id'

      def delete(self, request,id):
           product = get_object_or_404(Product,pk =id)
           if product.id > 40 :
                return Response({'error':'Product Can not be deleted, it is above 49, have mercy'})
           product.delete()

           return Response(status= status.HTTP_204_NO_CONTENT) 







Now, After doing this, We have to go back to our urls file and regester this model set




router = SimpleRouter()
router.register('Product',views.ProductViewSet())

































































































...
