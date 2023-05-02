
This is the projects url file

urlpatterns = [
    path('store/',include('store.urls'))
]



This is the apps url file
Here we say tht we want to go the end url of the products and only accept numbers ass the params


urlpatterns = [
     path('product-details/<int:id>',views.product_details)
]



This is the file in the views file. Here we cerive the request and the id

@api_view()
def product_details(request,id):

    return Response(id)







HERE IS MORE EXPLANATION
****************************************************************************************************************************************************************

In Django REST framework, you can define API views using class-based views or function-based views. Here are some code samples for both approaches:


Class-based views:
  
  
  from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, world!'
        }
        return Response(data)


In this example, we define a class-based view HelloAPIView that extends APIView. We define a get method that returns a response with a simple JSON message.



Function-based views:
  
  from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    data = {
        'message': 'Hello, world!'
    }
    return Response(data)




In this example, we define a function-based view hello using the api_view decorator. We specify that this view only handles GET requests.
We then define a data dictionary containing the message we want to return and return a response with that data.

Both of these examples define a simple API view that returns a JSON response with a message. 
You can modify these examples to perform more complex logic, such as querying a database, validating input data,
or serializing data to return in the response.


















































































...
