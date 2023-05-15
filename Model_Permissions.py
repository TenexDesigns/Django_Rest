
1.



from django.db import models

class MyModel(models.Model):
    # Model fields here

    class Meta:
        permissions = [
            ('view_history', 'Can view History'),  // The first value is the code  name for the permission, The second value is the description for the permission
            ('change_mymodel', 'Can change MyModel'),
            ('delete_mymodel', 'Can delete MyModel'),
        ]




2.

Run the database migrations to create the necessary tables and permissions:

python manage.py makemigrations
python manage.py migrate





3. In our Viewset for our model , we are going to addd an actio to carry out the custom action that the permssiion gives


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True) # We have detail is true, because this is for a particular customer
    def history(self,request,pk): #we have pk, Because this is for a particular customer
        return ('Ok')





4. Then we are going to make a permission class

class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('store.view_history')  // Here we check if the user has Permission to view the history, If he has permission, then they will be allowed to view the history




5.We give the intented view set that wants to see the permisssion , that permiision

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True,permission_classe=[ViewCustomer_History_permssiion]) # We have detail is true, because this is for a particular customer
    def history(self,request,pk): #we have pk, Because this is for a particular customer
        return ('Ok')



MORE EXPLANATION
***********************************************************************************************





In Django, model permissions allow you to define and enforce access control at the object level. They provide a way to restrict operations on individual instances of a model based on user permissions.

To use model permissions in Django, you need to follow these steps:

Define the desired model permissions in your Django model class by specifying the permissions attribute. This attribute is a list of permission tuples, where each tuple consists of a permission code (in uppercase) and a human-readable permission name.
python
Copy code
from django.db import models

class MyModel(models.Model):
    # Model fields here

    class Meta:
        permissions = [
            ('view_mymodel', 'Can view MyModel'),
            ('change_mymodel', 'Can change MyModel'),
            ('delete_mymodel', 'Can delete MyModel'),
        ]
In the example above, the MyModel class specifies three model permissions: view_mymodel, change_mymodel, and delete_mymodel. These permissions allow users to view, change, and delete individual instances of MyModel.

Run the database migrations to create the necessary tables and permissions:
shell
Copy code
python manage.py makemigrations
python manage.py migrate
Running the migrations will create the corresponding database tables and permission entries.

Assign the model permissions to users or groups using Django's authentication and authorization system. You can do this through the Django admin site or programmatically.
Assigning permissions to users:
python
Copy code
from django.contrib.auth.models import User

user = User.objects.get(username='john')
user.user_permissions.add('myapp.view_mymodel', 'myapp.change_mymodel', 'myapp.delete_mymodel')
In the example above, the view_mymodel, change_mymodel, and delete_mymodel permissions are assigned to the john user.

Assigning permissions to groups:
python
Copy code
from django.contrib.auth.models import Group

group = Group.objects.get(name='admins')
group.permissions.add('myapp.view_mymodel', 'myapp.change_mymodel', 'myapp.delete_mymodel')
In this example, the view_mymodel, change_mymodel, and delete_mymodel permissions are assigned to the admins group.

Use the model permissions in your views or view sets to enforce access control based on user permissions. Django provides helper functions like has_perm() and get_perms() to check for permissions.
python
Copy code
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_mymodel')
def mymodel_detail(request, pk):
    mymodel = get_object_or_404(MyModel, pk=pk)
    # Your implementation here
In the example above, the permission_required decorator is used to ensure that only users with the view_mymodel permission can access the mymodel_detail view.

By using model permissions in Django, you can control access to individual instances of a model based on the permissions assigned to users or groups. This allows for fine-grained access control within your application.






explain DjanoModelPermissions
*******************************************************************************************************************************************************

DjangoModelPermissions is a built-in permission class provided by Django REST Framework (DRF) that allows object-level permissions based on Django's model-level permissions. It determines the access permissions for individual model instances based on the user's model-level permissions.

When DjangoModelPermissions is applied to a view or viewset, it performs the following checks:

It checks if the user making the request is authenticated. If the user is not authenticated, access is denied, and a "401 Unauthorized" response is returned.

If the user is authenticated, it checks if the user has the necessary model-level permissions for the requested action (e.g., view, add, change, or delete) on the model associated with the view or viewset.

If the user has the required model-level permission, access to the object is granted, and the request is processed.

If the user does not have the necessary model-level permission, access is denied, and a "403 Forbidden" response is returned.

To use DjangoModelPermissions in your Django REST Framework views or viewsets, you need to include it in the permission_classes attribute of your view or viewset.

Example usage in a viewset:


from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

class MyModelViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
In the example above, the MyModelViewSet class-based viewset uses DjangoModelPermissions as the permission class. This means that the viewset will check the model-level permissions of the authenticated user before allowing access to the individual model instances.

Note that DjangoModelPermissions works in conjunction with Djangos built-in model-level permissions. Therefore, you need to define the model-level permissions for your models using Django's permission system (view, add, change, and delete) for DjangoModelPermissions to enforce those permissions.

By using DjangoModelPermissions, you can easily incorporate model-level permissions into your DRF views and viewsets, ensuring fine-grained access control over individual instances of your models.










































































...
