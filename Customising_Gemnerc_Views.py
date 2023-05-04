Generic Views alredy do a lot of things for us outside the box,


for example, This one, handlses all the get,post ,put and patch for us 


class Product_details(RetrieveUpdateDestroyAPIView):
      queryset =  Product.objects.all()
      serializer_class = ProductSerializer





      
      This is because the  the RetrieveUpdateDestroyAPIView provides us a level of abstatction by handling allof the above methods
      here is its code
      
      class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)













How ever we may want to give custome responses to certain Http methods, you will have to overide thses methods,
For example , Here we may want to customise out delete method and addd some logic  and even addd a custome message
e.g

Here we have overiden the delete method and added some logic and even a custom message.
We have customised our Generic view.



class Product_details(RetrieveUpdateDestroyAPIView):
      queryset =  Product.objects.all()
      serializer_class = ProductSerializer
      lookup_field = 'id'

      def delete(self, request,id):
           product = get_object_or_404(Product,pk =id)
           if product.id > 40 :
                return Response({'error':'Product Can not be deleted, it is above 49, have mercy'})
           product.delete()

           return Response(status= status.HTTP_204_NO_CONTENT) 







          HERE IS MORE EXPLANATION
*******************************************************************************************************************************************************************

There are different ways to customise concrete view classes or generic view classes in Django REST framework123:

You can override the class attributes, such as queryset, serializer_class, permission_classes, etc.,
to specify the model, serializer, and permissions for your view. For example:

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]



You can override the methods on the view class, such as get_queryset(), get_serializer_class(), get_object(), etc.,
to provide custom logic for retrieving or modifying the data. For example:



from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        # Filter the books by the genre query parameter
        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            return Book.objects.filter(genre=genre)
        return Book.objects.all()



You can use mixins to add extra functionality to your view class, such as pagination, filtering, ordering, etc. For example:


from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Add pagination by 10 per page
    pagination_class = generics.pagination.PageNumberPagination
    pagination_class.page_size = 10
    # Add filtering by title or author
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    # Add ordering by title or published date
    filter_backends.append(filters.OrderingFilter)
    ordering_fields = ['title', 'published_date']





You can create your own custom view classes by subclassing an existing concrete view class and overriding its attributes or methods. For example:


from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class CustomBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # Add some custom logic when creating a new book
        serializer.save(owner=self.request.user)



These are some examples of how to customise concrete view classes or generic view classes in Django REST framework.
You can also refer to the documentation12 or some tutorials3 for more details and examples




          HERE IS MORE EXPLANATION
*******************************************************************************************************************************************************************

Sure, here are a few examples of how to customize Concrete View Classes or Generic View Classes in Django Rest Framework with code samples:

Customizing CreateAPIView

from rest_framework.generics import CreateAPIView
from .serializers import MyModelSerializer
from .models import MyModel

class MyCustomCreateAPIView(CreateAPIView):
    serializer_class = MyModelSerializer

    def perform_create(self, serializer):
        # Add additional logic before or after creating the object
        instance = serializer.save()
        # Perform additional actions on the object instance
        instance.some_attribute = 'some value'
        instance.save()
In this example, we define a custom view MyCustomCreateAPIView that inherits from the CreateAPIView class. We specify a serializer class as before, but we also override the perform_create method. This method is called when a POST request is made to create a new object.

We can add additional behaviors to this method, such as performing validation or adding additional data to the object being created. In this example, we call the save method on the serializer to create the object, and then perform additional actions on the resulting object instance.

Customizing ListAPIView

from rest_framework.generics import ListAPIView
from .serializers import MyModelSerializer
from .models import MyModel

class MyCustomListAPIView(ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_queryset(self):
        # Add additional filtering or sorting to the queryset
        queryset = super().get_queryset()
        return queryset.filter(some_attribute='some value')
In this example, we define a custom view MyCustomListAPIView that inherits from the ListAPIView class. We specify a queryset and serializer class as before, but we also override the get_queryset method. This method is called to retrieve the queryset of objects to be displayed.

We can add additional filtering or sorting to the queryset, such as only showing objects with a specific attribute value. In this example, we call the super() method to retrieve the default queryset, and then add additional filtering to only show objects with a specific attribute value.

Customizing RetrieveAPIView

from rest_framework.generics import RetrieveAPIView
from .serializers import MyModelSerializer
from .models import MyModel

class MyCustomRetrieveAPIView(RetrieveAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_object(self):
        # Add additional logic to retrieve the object
        obj = super().get_object()
        # Perform additional actions on the object instance
        obj.some_attribute = 'some value'
        obj.save()
        return obj
In this example, we define a custom view MyCustomRetrieveAPIView that inherits from the RetrieveAPIView class. We specify a queryset and serializer class as before, but we also override the get_object method. This method is called to retrieve a single object by its primary key.

We can add additional logic to retrieve the object, such as checking permissions or adding additional data to the object instance. In this example, we call the super() method to retrieve the default object, and then perform additional actions on the resulting object instance.

Customizing UpdateAPIView

from rest_framework.generics import UpdateAPIView
from .serializers import MyModelSerializer
from .models import MyModel

class MyCustomUpdateAPIView(UpdateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def perform_update(self, serializer):
        # Add additional logic before or after updating the object
        instance = serializer.save()
        # Perform additional actions on the object







         HERE IS MORE EXPLANATION
*******************************************************************************************************************************************************************








Customizing concrete view classes or generic view classes in Django REST framework involves overriding class attributes, creating custom base classes, or overriding methods on the view class. Here are some examples to demonstrate these techniques:

Overriding class attributes:
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
In this example, we override the queryset, serializer_class, and permission_classes attributes to customize the behavior of the ListCreateAPIView github.com.

Overriding methods on the view class:
from rest_framework import generics
from rest_framework.response import Response

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
In this example, we override the list method to customize the behavior of the ListCreateAPIView when listing objects github.com.

Creating custom base classes:
from rest_framework import generics

class BaseRetrieveView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    pass

class BaseRetrieveUpdateDestroyView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
In this example, we create custom base classes by combining a MultipleFieldLookupMixin with the existing RetrieveAPIView and RetrieveUpdateDestroyAPIView. These custom base classes can be used throughout the project for consistent behavior django.fun.

These techniques allow you to customize and reuse behaviors across different views in your Django REST framework application.





















































































































































...
