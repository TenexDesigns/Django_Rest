

Actions are the methods in view sets that respond to requests

We can define a custome action , since In a model view set the actions for creating deletiong and updating have alredy been defined 

To create a custome action

from rest_framework.decorators import action,


         @action(detail=False,  -> If this is false, it meas that this end poit will be availabele on the list view e.g 127.0.0.1:8000/store/customers/me, if this is true, then this end poiunt will be avaliale o h=the specific detil of e,g a customer 127.0.0.1:8000/store/customers/1/meas oppsed to the list.
        def me(self, request):




e.g in the customers view set 
                 
                 
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
   # permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'],)   --> We indicate the methods we want to be alllowed on this end point
    def me(self, request):
        (customer,created) = Customer.objects.get_or_create(    ----> Whe we use the method, get_orCreaete -> this method returns a tuple of the gottten or creted customer, and a boolen value, which we sav e in creted
            user_id=request.user.id)                 --> We fetch th customer based on the user id in the reust object that is sent togethert with th token
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)   // Here we update using the data gotten fromn the user
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
                 
                 
                 
                 
                 
                 
CREATING CUSTOME  ACTIONS
********************************************************************************************************************************************************************
   
To create custom actions in Django view sets, you can follow these steps:

1.Import the necessary dependencies:
                 
from rest_framework.decorators import action
from rest_framework.response import Response

                 
                 
2.Define your view set by inheriting from an appropriate base class, such as ModelViewSet:                 
   from rest_framework import viewsets

class MyViewSet(viewsets.ModelViewSet):
    # ... view set configuration ...
              
3.Add a method to the view set for your custom action. The method name will correspond to the action name. 
                 Decorate the method with the @action decorator, specifying the details of the action:              
                 
                 
  @action(detail=True, methods=['post'])
def custom_action(self, request, pk=None):
    # Custom logic goes here
    return Response({'message': 'Custom action performed'})
               
    
                 
                 
                 
                 
                 
                 In the example above, the custom_action method is defined as a custom action with the name "custom_action". 
                 The detail=True argument indicates that the action is performed on a specific resource, identified by pk (primary key). 
                 The methods argument specifies the allowed HTTP methods for the action. In this case, the action allows only the HTTP POST method.
                 
                
                 
4.Customize the method according to your requirements. You can access the current request (request), the primary key (pk) if needed, and perform any necessary operations.

5.Return a response from the method. You can use the Response class from rest_framework.response to construct the response. For example, returning Response({'message': 'Custom action performed'}) will send a JSON response with a message indicating that the custom action was performed.
                 
                 
By following these steps, you can create custom actions in Django view sets, extending the functionality of your API beyond the standard CRUD operations. Remember to associate the view set with appropriate URL patterns to map the custom action to the desired endpoint.           
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
MORE EXPLANTION ON ACTION
***********************************************************


In Django, view sets are a convenient way to define a set of related views (CRUD operations) for a particular model or resource. View sets typically correspond to RESTful APIs and provide a high-level abstraction for working with models.

Django view sets support various actions (methods) that can be performed on a resource. Here are some common actions available in Django view sets:

List: The list action retrieves a list of resources. It typically corresponds to the HTTP GET method and returns a serialized representation of all instances of the model.

Create: The create action is used to create a new resource. It corresponds to the HTTP POST method and accepts data to create a new instance of the model.

Retrieve: The retrieve action retrieves a single resource by its unique identifier. It corresponds to the HTTP GET method with a specific resource ID.

Update: The update action updates an existing resource. It corresponds to the HTTP PUT or PATCH method and modifies the fields of the resource identified by its ID.

Partial Update: The partial_update action is similar to the update action but allows for partial updates. It corresponds to the HTTP PATCH method and modifies only the specified fields of the resource.

Delete: The destroy action deletes an existing resource. It corresponds to the HTTP DELETE method and removes the resource identified by its ID.

Additionally, Django view sets can support custom actions beyond the standard CRUD operations. Custom actions are defined by adding methods to the view set with appropriate names and decorators.

For example, you can define a custom action named custom_action in a view set:


from rest_framework.decorators import action
from rest_framework.response import Response

class MyViewSet(viewsets.ModelViewSet):
    # ... view set configuration ...

    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        # Perform custom logic here
        # Retrieve the instance using 'pk'
        instance = self.get_object()
        # Do something with the instance
        # Return a response
        return Response({'message': 'Custom action performed'})
In the example above, the custom_action method is defined as a custom action using the @action decorator. It corresponds to the HTTP GET method and performs custom logic on an individual resource.

These actions in Django view sets provide a convenient way to handle various operations on resources and customize the behavior of your API endpoints.





































































