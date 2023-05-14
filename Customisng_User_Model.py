So the user model provided to us by the django authentification system is good, but we may want to extend the user infoemation it holds.
This is the user information it currently holds, without any modifction, But we may want to customise it and extend it so that this user model holds more information.

 id | password|last_login|is_superuser|username|first_name|last_name|email            |is_staff|is_active|date_joined
 1,   pbkdf2,    2023-05-,   true,      Tenex,  "George",  "Gacau",   muny7@gmail.com,   true,   true,     2023-05-08


THERE ARE TWO WAYS OF EXTENDING THE USER MODEL TO HOLD MORE INFORMATION


1.EXTEND USER MODEL THROUH INHERITANCE

user model  
    |
    | (Appuser model inherits from the user model)
    |
    |
    V 
app user model

Here we use inheritance to extend the user model
We create another model called app user  ,and this model should extend or inherit the user model in django









2.THEOUGHT CREATING PROFILE


profile model --------------> user model
                   |
               (this is a one to one relationship between appuser nad user mode)

The other option is to create a profile.
We create a profile model and add a one to one  link to the user model
So in this scenario we are not using inheritance, WE ARE USING COMPOSITION, by esatblishing a one to one relationship between user model and app user model.
So the profile model is composed of a user model





DIFFERNECES OF THE TWO METHODS AND THEIR ADVANTAGES AND DISAVANTAGES


With the first approach, we will end up etending the user table in the database,. This means any extra atributes we add in our exteded model will end up in this table  making that table have more fields in the database .
With the second approach, we are not going to extend this table, we are going to have a separate table and in that table we will have a foreign key to the user table
We can not use the first approach in the middle of a project, as it can cause migration issues, so most of the time we are going to use the second approach


BEST ADVICE

USe the first approach to store attributes related to authenfcation process e.g phone number , anything extra should go to the profile table e.g birt date, address, nick name 
With this oncept we allow each app to ahve a different concept of a profile model, e.g the sales app, can ahve the customer model as the profile model, and the training app can have the stident model as the profile model and store the related data to the student table instead of extenfing it to the user model.

We can not use the first approach in the middle of a project, so most of the time we are going to use the seconf approach
Remember that changing the user model after the project has started and data has been collected can be challenging.
Its best to plan the user model customization before starting the project to avoid data migration issues.






MORE EXPLAANTION
****************************************************************************************************************

IN OUR PROJECT, WE DECIDE TO CREATE A CORE APP THAT WILL HAVE THE EXTED USERS MODEL. This core app will be specific to our project , and it is where we can write changes that can affect the whol e project and where we can write code that can be we can bepend upone from other app in the project , since this app is specific to our project and its app


1. Create a new model for your custom user by subclassing the AbstractUser or AbstractBaseUser class provided by Django. 
If you want to extend the existing User model, use AbstractUser. If you want to start from scratch, use AbstractBaseUser. Heres an example using AbstractUser
#core APP
models.py

from django.db import models
from django.contrib.auth.models import AbstractUser  //If you want to extend the existing User model, use AbstractUser.


class User(AbstractUser):
    email = models.EmailField(unique=True)  // This is the change we made to the existing user model, we made the emal unique, we didnt create a new user model, we just made some changes to the existing one, that is why we used the AbstarctUser method


#core app
Admin.py

from django.contrib import admin                                   //We give the userAdmin an alias name of BaseUserName to avoid name clashing 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  // Here we are using the existing usr admin and just making  slite modifications so that the email and first and last name can be see on the admins page



@admin.register(User)                                                // Here is where we regester the custome user that we created so that it can be seen on the admins site. 
class UserAdmin(BaseUserAdmin):
        add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","email","first_name","last_name"),
            },
        ),
    )


#proctes folder
settings.py

AUTH_USER_MODEL = 'core.User'  // We add this to show django that we changed the Uer model that we are using and that we are using the one we modified in the core model
                              // So any refernces to the user model should be made to this user moel here that we have registered
                              // Here is an example


IN ANOTHER APP CLAEED LIKES , WE HAVE A REFENCE TO THE USER MODEL, BUT WE CHANGED THE DEFAULT USER IMPLEMNATION AND SO WE HAVE TO REFERENCE THE ONE THAT WE HAVE CREATED AND REGISTERED IN THE SETTINGS E.G

#likes App
models.py

from django.conf import settings                             // Use this insted of User
#from django.contrib.auth.models import User                   Do  not use this 

class LikedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

























































































































...
