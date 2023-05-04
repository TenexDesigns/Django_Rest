
Viewsets in Django REST framework are classes that provide CRUD (Create, Retrieve, Update, Delete) operations for a particular model or database query. 
Instead of writing separate views for each CRUD operation, viewsets provide a more organized and efficient way to handle them.

To use viewsets, we also need to define a router to map the URLs to the appropriate views.
Here is an example of how to define a viewset and router for a simple Book model:



from rest_framework import viewsets, routers
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)






In this example, we define a BookViewSet that inherits from the ModelViewSet class, which provides all the CRUD operations for the Book model. We also define 
a queryset attribute to retrieve all Book instances and a serializer_class attribute to use the BookSerializer to serialize and deserialize the data.



We then define a DefaultRouter instance and register the BookViewSet with the books endpoint. This will generate the following URL patterns:


  /books/
/books/{book_id}/



Now we can create, retrieve, update, and delete Book instances using the appropriate HTTP methods on the /books/ endpoint.



TO CUSTOMISE THE GET,POST,PUT AND DELETE MTHODS OF THE VIEW SET


To customize a viewset for the create, delete, put, and post HTTP methods,
you can define methods with the appropriate names in your viewset class. Here's an example:


from rest_framework import viewsets
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=204)

    def partial_update(self, request, pk=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)




In this example, we define the create(), update(), destroy(), and partial_update() methods on the BookViewSet class.
Each of these methods corresponds to a specific HTTP method (POST, PUT, DELETE, PATCH), and takes a request object as its argument.


In each method, we first get the Book instance (if applicable) using the get_object() method. 
We then create a new BookSerializer instance using the request data and any relevant arguments.
We check if the serializer is valid, and if so, save the data and return a Response object with the appropriate status code.



Note that when defining custom methods on a viewset, you should always include a return Response() statement to return a response to the client. 
Also, when defining custom methods for update and partial update actions, you should include a pk parameter to identify the specific object being updated.














One of the advantages of using viewsets is that they provide a consistent and predictable API structure, 
which can be customized by defining additional actions or overriding existing ones.
Heres an example of how to add a custom action to the BookViewSet:



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        book = self.get_object()
        book.is_published = True
        book.save()
        return Response({'status': 'published'})





In this example, we define a new publish action that will set the is_published attribute of a Book instance to True. 
We use the @action decorator to define the new action and specify that it should be invoked using the POST method on a specific Book instance.



We can then register this new action with the books endpoint by passing the name parameter to the register() method:


router.register(r'books', BookViewSet, basename='book')
router.register(r'books/(?P<book_pk>[^/.]+)/publish', BookPublishViewSet, basename='book-publish')



Now we can invoke the publish action by making a POST request to the /books/{book_id}/publish/ endpoint.

In summary, viewsets provide a more efficient and organized way to handle CRUD operations, and routers help to map the URLs to the appropriate views.
Custom actions can also be added to viewsets to provide additional functionality beyond the default CRUD operations.























































































.....
