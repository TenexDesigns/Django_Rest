Here insted of using functions we use classes and we use the APIVies. Then in the urls folder we have to do this 

urlpatterns = [
    path('products/',views.ProductList.as_view()),
    path('product-details/<int:id>',views.Product_details.as_view())
]




This is our vies file



from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store.models import Product
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import Product
from .serialisation import ProductSerializer




class ProductList(APIView):
      def get (self,request):
           queryset = Product.objects.select_related('collection')
           serializer = ProductSerializer(queryset, many =True)
           return Response(serializer.data)
      def post(self,request):
           serializer = ProductSerializer(data = request.data)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           print(serializer.data)
           return Response(serializer.data)
              

# @api_view(['POST'])
# def product_list(request):
#     if request.method == 'GET':
#        queryset = Product.objects.select_related('collection')
#        serializer = ProductSerializer(queryset, many =True)
       
#        return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer.data)
#         return Response(serializer.data)
    
        
    

class Product_details(APIView):
      

      def get(self,request,id):
        product = get_object_or_404(Product,pk =id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
      def put(self,request,id):
        product = get_object_or_404(Product,pk =id)
        serializer = ProductSerializer(product,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
      def delete(self,request,id):
          product = get_object_or_404(Product,pk =id)
          product.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

             

            
            
            
            
            
            
            
            
 HERE IS MORE EXPLANTION           
*******************************************************************************************************************************
            
  Class-based views are a way of creating views in Django that use classes instead of functions.
They can help you structure your views and reuse code by harnessing inheritance and mixins. 
They also provide some generic views for common tasks, such as displaying a list or a detail of an object1.

A class-based view is a subclass of django.views.generic.View, which is a base class that implements the basic logic of handling HTTP requests.
The View class has a method for each HTTP method (get, post, put, delete, etc.) that returns a HttpResponse object or raises an exception.
By default, these methods return a HttpResponseNotAllowed response, indicating that the view does not accept the request method1.

To create a class-based view, you need to override one or more of these methods and provide your own logic for handling the request. 
For example, here is a simple view that returns a plain text response for GET requests1:          
            
            # some_app/views.py
from django.http import HttpResponse
from django.views.generic import View

class GreetingView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")
            
            
            
     To use this view in your URLconf, you need to call the as_view() class method, which returns a function that can be used as a view1:       
            
            
        # urls.py
from django.urls import path
from some_app.views import GreetingView

urlpatterns = [
    path("greeting/", GreetingView.as_view(), name="greeting"),
]    
            
            
     This will map the URL /greeting/ to the GreetingView view.

However, writing your own class-based views from scratch can be tedious and repetitive. 
That’s why Django provides some generic class-based views that already implement some common functionality for you. 
These generic views are subclasses of View that override some methods and attributes to provide specific behavior1.

For example, Django has a generic ListView class that can display a list of any kind of object.
This view automatically queries the database for all objects of the specified model and passes them to the template as a variable named object_list. 
You can customize the view by overriding attributes or methods, such as model, template_name, context_object_name, get_queryset, get_context_data,
paginate_by, etc2.

Here is an example of using the generic ListView class to display a list of books2:       
            
            
            # some_app/views.py
from django.views.generic import ListView
from some_app.models import Book

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
            
            
            
       This view will query the database for all books and pass them to the template as a variable named books.
You can also specify the template name and the context object name as attributes.

To use this view in your URLconf, you need to call the as_view() class method, just like before2:     
            
            
            
            
            
           # urls.py
from django.urls import path
from some_app.views import BookListView

urlpatterns = [
    path("books/", BookListView.as_view(), name="books"),
] 
            
            
            
            
       This will map the URL /books/ to the BookListView view.

For more information and examples on class-based views, you can check out the following resources:     
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            







HERE IS MORE EXPLANATION
*******************************************************************************************************************************

There are three main approaches for implementing views in Django openclassrooms.com:

Function-based views - the request is handled by one function, with different request types such as POST and GET managed by conditional statements.
Class-based views subclassing django.views.generic.View - the request is handled by a class, with different request types being managed by separate methods.
Generic class-based views - the request is handled by a generic class-based view, which allows you to avoid writing commonly-used view logic.




The choice of which type of view to use often comes down to personal preference and project requirements.
Some developers prefer to use generic views whenever possible to reduce their workload, 
while others prefer class-based views subclassing django.views.generic.View for better readability.
Function-based views may be chosen for their simplicity and ease of understanding, 
especially in projects that do not share large chunks of code between views.





Class-based views in Django provide an object-oriented way to organize your view code, making it more reusable and better organized.
They were introduced as an alternative to function-based views, which were available in Django before class-based views.





Heres a simple example of a class-based view:
    
    
    # views.py
from django.views import View

class SimpleClassBasedView(View):
    def get(self, request):
        # code to process a GET request

    def post(self, request):
        # code to process a POST request



To include a class-based view in a URL pattern, you need to use the as_view() method.
This is one of the utility methods that you have access to due to inheriting from django.views.View


# fotoblog/urls.py
urlpatterns = [
    ...
    path('', authentication.views.SimpleClassBasedView.as_view(), name='simple_view'),
    ... 
]





Generic class-based views in Django provide extra common functionality.
For example, a common type of view might be called a template view, which generates some context and sends the context to a specified template for rendering.
Django provides a generic class-based view for that very purpose, TemplateView




# views.py
from django.views.generic import TemplateView

class ShowTimeView(TemplateView):
    template_name = 'show_time.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context


























































































































....
