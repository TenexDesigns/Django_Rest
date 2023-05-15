Permissions in Django REST Framework (DRF) allow you to control access to your API endpoints based on certain rules or conditions.
Permissions determine whether a user is allowed to perform a certain action, such as viewing, creating, updating, or deleting a resource.

DRF provides a range of built-in permission classes that you can use to define the access control rules for your API views. 
Here are some commonly used permission classes:


IsAuthenticated: Requires the user to be authenticated (logged in) to access the endpoint. If the user is not authenticated, they will receive a "401 Unauthorized" response.

IsAdminUser: Requires the user to be authenticated and have the is_staff flag set to True in the user's account. This permission is suitable for admin-only access.

AllowAny: Allows unrestricted access to the endpoint. This is the default permission class if no other permission is specified.

IsAuthenticatedOrReadOnly: Allows read access to any user (authenticated or anonymous) but only allows write access (create, update, delete) to authenticated users.

DjangoModelPermissions: Provides object-level permissions based on the Django model's view, add, change, and delete permissions. Requires the user to be authenticated, and the user must have the required permissions for the specific model and action.

DjangoObjectPermissions: Provides fine-grained object-level permissions based on Django's model-level permissions. Requires the user to be authenticated, and the user must have the required permissions for the specific model and action



  
  These are just a few examples of the built-in permission classes in DRF.
  You can combine multiple permission classes or create your custom permission classes by subclassing BasePermission and implementing the has_permission() 
  or has_object_permission() methods.

To apply permissions to your API views, you can define the permission_classes attribute in your view or view set. For example:



from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    # ... view implementation ...



In the example above, the MyAPIView class specifies the IsAuthenticated permission class, meaning that only authenticated users can access this view.

You can also set permissions at the project-wide level by modifying the DEFAULT_PERMISSION_CLASSES setting in your Django settings module.

By utilizing permissions in Django REST Framework, you can effectively control access to your API endpoints based on your application's requirements and security needs.





APPLYING PERMISSIONS
**********************************************************************

1. APPLYING THEM GLOBALY OR AT THE PROJECT LEVE
The default permission is usally allow any, allowing all users  to access all endpoints

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',   --> Here all our endpooints are closseed off to annomys uses, only athenticated usrw can access theses endpoints 
    ],                                                  --> However we can allways overide this peremisssions ob=n specifc views ,by using the permissionclasses option
    # Other DRF settings...
}



2.Applying multiple permissions to a view:
  
  from rest_framework.permissions import IsAuthenticated,
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated, ]   ---> This means that our endpoint and all actions in it is clossed of to all anonymous users and only authenticated users are allowed

    def get(self, request):
        # Your implementation here
        return Response({'message': 'This is an admin-only endpoint'})



In this example, both IsAuthenticated and IsAdminUser permission classes are applied to the MyAPIView.
Only authenticated users who are also staff members (admin users) will have access to the GET request.


different persmiisions for different actions like create, retrieve, list and destroy

class MyAPIView(ModelViewset):
  permission_classes =[AllowAny()]           ----> tHIS ALOWS ALL USES EVEN ANOMYOUS ONES TO ACCESS THIS END POINT
    
    def get_permissions(self):
      if self.request.method =='DESTROY:  --> bUT THE DESTROY ACTION IS RESTRICTED TO AUTHENTICARTED USERS ONLY
         return[IsAuthenticated()]
      RETURN [AllowAny()]  -----> This means that any other end point anonyous usr are alloowed to view it.
      
    def get(self, request):
        # Your implementation here
        return Response


3.Applying multiple permissions to a view:
  
  
  from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        # Your implementation here
        return Response({'message': 'This is an admin-only endpoint'})

In this example, both IsAuthenticated and IsAdminUser permission classes are applied to the MyAPIView.
Only authenticated users who are also staff members (admin users) will have access to the GET request.

4,Appling Permissions to actions

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]               -----> This is the permision applied to this end point 

    @action(detail=True, permission_classes=[AllowAny])   ---> When detail is True, it means this method will be applied on the detail instard of the list end point , The permission applied here overides that which was sert for this end point 
    def history(self, request, pk):
        return Response('ok')


      
      
      
      
      
      
      
      
      
      
      
      
      

MAKING CUSTOME PERMISSIONS
********************************************************************************************************************************************************

TO MAKE CUSTOME PERSMIISIONS, WE NEED TO CHECK HOW THE DEFAULT PERMSISIONS ARE IMPLEMENTED ,  SO THATWE CAN COPY THEM OR LEARN FROM THEM

THIS IS HOW THE IsAuthenticated Permission is implemented

class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)



SO IN OUR CUSTOM IMPLEMETATION OF A PERMISSION , WE HAVE TO INHERIT THE BASEPERMISSION CLASS AND OVERIDE OR MAKE MODIFICATIOS TO THE has_permission method

For example here , we check if the method is a get method, and allow for that opeation to be done only, but all other opreations need the user to be authenticated(is_staff) Meaning they have permission

class IsUser(BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        return  bool(request.user and request.user.is_staff)




HOEVER, ALLOWING THE GET METHOD ONLY IS BAD AS IT INHIBST OTHER METHODS LIKE HEAD AND OPRIONS
The get,head and options methods are what are called safe methods. So we need to allow all of theses mer=thods to be accesed without neeed for usr authentication


class IsUser(BasePermission):
    def has_permission(self, request, view):
       if request.method in permissions.SAFE_METHODS:
            return True
        return  bool(request.user and request.user.is_staff)



      
      
      
      
      
      
      
CUSTOM PERMISSSIONS 
      **************************************8


To create a custom permission class in Django, you can follow these steps:

Import the necessary dependencies:

from rest_framework.permissions import BasePermission
Define your custom permission class by subclassing BasePermission and implementing the has_permission() or has_object_permission() method:
python
Copy code
from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # Custom permission logic goes here
        # Return True if the permission is granted, False otherwise
        return True  # Replace with your permission logic
In the example above, the CustomPermission class is defined as a custom permission by subclassing BasePermission and implementing the has_permission() method.
You can implement your custom permission logic within this method.

Implement the has_object_permission() method if you need to perform object-level permission checks:

from rest_framework.permissions import BasePermission

class CustomObjectPermission(BasePermission):
    def has_permission(self, request, view):
        # Custom permission logic for view-level permission
        return True  # Replace with your permission logic
    
    def has_object_permission(self, request, view, obj):
        # Custom permission logic for object-level permission
        return True  # Replace with your permission logic
In the example above, the CustomObjectPermission class implements both has_permission() and has_object_permission() methods.
The has_permission() method is used for view-level permission checks, while the has_object_permission() method is used for object-level permission checks.

Use your custom permission class in a view or view set:

from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    permission_classes = [CustomPermission]

    def get(self, request):
        # Your implementation here
        return Response({'message': 'Custom permission applied'})
In the example above, the CustomPermission class is added to the permission_classes attribute of the MyAPIView class-based view. This ensures that the custom permission logic defined in CustomPermission is applied to the view.

You can apply the custom permission class to a view set in a similar way by specifying permission_classes in the view set configuration.

By creating custom permission classes in Django, you have full control over the permission logic in your API views. You can customize the behavior based on your application's requirements, such as checking user roles, additional conditions, or integration with external systems.
























.....
