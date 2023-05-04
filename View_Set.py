
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


from django.urls import include, path
from rest_framework import routers
from .views import Books

router = routers.DefaultRouter()
router.register(r'product', views.products)

urlpatterns = [
    path(r'', include(router.urls)),
]







HERE IS MORE EXPLANATION
*************************************************************************************************************************************************************


In Django Rest Framework, a ViewSet is a high-level abstraction that allows developers to combine common functionality for multiple views into a single class. 
A ViewSet can handle a variety of HTTP methods, including GET, POST, PUT, PATCH, and DELETE, among others.


There are several types of ViewSets in Django Rest Framework, including:
      
      
ModelViewSet: This provides CRUD (Create, Retrieve, Update, Delete) operations for a Django model.
            It is a combination of APIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin.

ReadOnlyModelViewSet: This provides only read operations (i.e. GET) for a Django model. It is a combination of APIView,
      ListModelMixin, and RetrieveModelMixin.

GenericViewSet: This is a ViewSet that doesn't provide any default implementations of actions, and expects the developer
      to explicitly define the actions that they want to support. It is a combination of APIView and ViewSetMixin.

ViewSet: This is a ViewSet that provides basic CRUD (Create, Retrieve, Update, Delete) operations. It is a combination of APIView and ViewSetMixin.

Heres an example of how to define a basic ViewSet:




      
      from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class MyViewSet(ViewSet):
    def list(self, request):
        # Handle GET request to retrieve all objects
        return Response({'message': 'This is a list view'})

    def retrieve(self, request, pk=None):
        # Handle GET request to retrieve a single object by its primary key
        return Response({'message': f'This is a detail view for object {pk}'})

    def create(self, request):
        # Handle POST request to create a new object
        return Response({'message': 'This is a create view'})

    def update(self, request, pk=None):
        # Handle PUT request to update an existing object by its primary key
        return Response({'message': f'This is an update view for object {pk}'})

    def partial_update(self, request, pk=None):
        # Handle PATCH request to partially update an existing object by its primary key
        return Response({'message': f'This is a partial update view for object {pk}'})

    def destroy(self, request, pk=None):
        # Handle DELETE request to delete an existing object by its primary key
        return Response({'message': f'This is a delete view for object {pk}'})







In this example, we define a custom ViewSet MyViewSet that inherits from the base ViewSet class. 
We define several methods to handle different HTTP methods (i.e. list, retrieve, create, update, partial_update, and destroy) 
and return a simple response with a message.

To wire up the ViewSet to URLs, we can use a Router and register the ViewSet as a resource:


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'my-viewset', MyViewSet, basename='my-viewset')
urlpatterns = router.urls



This will automatically generate the URLs for the ViewSet, including routes for the different HTTP methods.





HERE IS  MORE EXPLANATION
*************************************************************************************************************************************************************

In Django REST Framework (DRF), ViewSets are a powerful and convenient way to organize your API views, 
allowing you to combine the logic for a set of related views in a single class django-rest-framework.org. 
They can be used to define basic CRUD operations for a model-based API, such as list, create, retrieve, update, and delete studygyaan.com.

A ViewSet class is a type of class-based View that doesn't provide method handlers such as .get() or .post(), 
but instead provides actions such as .list() and .create() django-rest-framework.org. ViewSets can be used with DRF routers, 
which automatically determine the URL configuration for you,
removing the need to explicitly register the views in the URL configuration django-rest-framework.org.




There are two main types of ViewSets in DRF: ViewSet and GenericViewSet testdriven.io.

ViewSet: This class extends APIView and provides the base set of view behavior testdriven.io. To use a ViewSet, you need to define
      the action implementations explicitly or use mixin classes.

GenericViewSet: This class extends GenericAPIView and provides the base set of generic view behavior along with the get_object and
      get_queryset methods testdriven.io.
      To use a GenericViewSet, you can override the class and either use mixin classes or define the action implementations explicitly.


Here's an example of a simple ViewSet for a model called Book


from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer






With this ViewSet, you can perform all CRUD operations on the Book model without having to write separate views for each operation.
You can use the built-in views provided by DRF or create your custom views as needed studygyaan.com.

ViewSets can be easily customized by using mixins and overriding methods. 
For example, you can override the get_queryset method to control the queryset used for the list view or the create 
method to add custom behavior to the create view studygyaan.com.

In summary, ViewSets in Django REST Framework provide a convenient and concise way to handle your API views, 
helping to keep your code organized and maintainable.
They can be used with DRF routers for automatic URL configuration and can be easily customized using mixins and overriding methods.







HERE IS MORE EXPLANATION
*************************************************************************************************************************************************************


View sets are a way to group related views in a single class in Django REST framework123. 
They are similar to generic view classes, but they do not provide any method handlers such as get() or post(), and instead provide actions 
such as list() and create().
View sets are useful when you want to create a consistent and concise API without having to write a lot of code for each view.
You can also use routers to automatically generate the URL patterns for your view sets.

There are two types of view sets in Django REST framework: ViewSet and ModelViewSet.
      The ViewSet class is a base class that allows you to define your own custom logic for each action.
      You can use mixins to add common functionality to your view set, such as listing, creating, updating, or deleting objects. For example:



from rest_framework import viewsets, mixins
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




The ModelViewSet class is a subclass of ViewSet that provides the default implementation of actions
for a model-backed API. It inherits from several mixins that provide the list(), create(), retrieve(), update(), and destroy() actions.
You only need to specify the model and the serializer for your view set. For example:



from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





You can also customise your view sets by overriding the attributes or methods of the base class or the mixins.
For example, you can change the queryset, the serializer class, the permission classes, the pagination class, the filter backends, etc.
You can also override the action methods or add custom actions to your view set. For example:


      
      from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add a custom action to get the best-selling books
    @action(detail=False)
    def best_sellers(self, request):
        best_sellers = Book.objects.filter(best_seller=True)
        serializer = self.get_serializer(best_sellers, many=True)
        return Response(serializer.data)





These are some examples of how to use view sets in Django REST framework. 
You can also refer to the documentation12 or some tutorials3 for more details and examples.







...
