To extend the user model in Django, you have a couple of options. Here is a step-by-step guide on how to do it:

1.Create a new Django app (if you don't already have one) using the following command in your project's root directory:

python manage.py startapp myapp
                           
2.In the models.py file of your newly created app (myapp), define your custom user model by subclassing AbstractUser or AbstractBaseUser.
 Heres an example using AbstractUser:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields here
    age = models.IntegerField(null=True, blank=True)
    # ... additional fields ...

    def __str__(self):
        return self.username
                           
3.In your projects settings.py file, update the AUTH_USER_MODEL setting to point to your custom user model. 
 This setting tells Django to use your custom model instead of the built-in User model:


AUTH_USER_MODEL = 'myapp.CustomUser'
                           
4.Run the following command to create the necessary database migrations:
                           
python manage.py makemigrations
                           
5.Apply the migrations to update your database schema:
                           
python manage.py migrate
                           
6.Now that your custom user model is set up, you can use it in your project. You can create users, authenticate them,
                           and perform other user-related operations as you would with the built-in User model. For example, you can create a new user like this:


from myapp.models import CustomUser

user = CustomUser.objects.create_user(username='john', password='password123')

7.By extending the user model, you can add your own fields and methods to the user model, allowing you to customize the user functionality in your Django application.























































































































...
