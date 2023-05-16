
SIGNALS

Per_save - FIred befoere a model is saved 
post_save - Fired after a model is saved 
pre_delete - Fired before a model is deleted
post_delete - Fired after a model is deleted


In our application we can listen to this nofications and do something



core app                               store app
create user                            create customer - > Listen to User..post_save signal and create a customer recored for that user




#App_Level
signals.py


define a function for your signal. This function is called a signal handleer
  from django.conf impoet settings
  from django.db.models.signals import post_save
  from django.dispatch import receiver
  from .models import Customer
 

@receiver(post_save,sender=settings.AUTH_USER_MODEL)   ///Now we don;t wan t to liste to the post save signal of every model in this project, we are only insteredted in the post saave event of the user model, that is why we specify the sender model, we specify the model we want to listen to in our sender
def create_customer_for_new_user(sender,**kwargs):
    if kwargs['created']:             //This returns a boolean value
       Customer.objects.create(user = kwargs['instance'])
        
        
  \\Lets telll django that this function should be called when a user model is saved
  \\To do that we import the receiver decolator, We pass in the receriver two arguments, one is the signal we want to receive
 
  
  
  THIS CODE IS NOT EXCUTED UNLESS WE IMPORT IT SOMEWHERE
 We go to the app.py file of our app and write this code
#App_leve
app.py
#Here we overide the ready method,
#THis method is called when this app is ready
    def ready(self) -> None:
        import store.signals.handlers





CREATING CUSTOM SIGNALS
A signal is simply an instance of the signmal class
We create a folder in the app level and give it the name of signals and we put there a ile claed __init.py


__init__.py

from django.dispath import Signal


order_created = Signal()  // now we need to fire this signal where an order is created



In the Order Serializer 

from .store.signals import order_creted

class Order serializer
       ****
    oreder_created.send_robust(self.__class__,order=oreder)  // We use send_robust to send the signal, we use self.__class__ to specify the sender, We can supply addintiona information is our signal , such as the order creted



So now we ahve a signal, that is fired when a order is creted,
Other apps can listen to this signal and do nesscear thins when nnedee




SIGNALS IN DJANGO
*****************************************************************************************************************************************************************



In Django, signals provide a way to allow decoupled applications to get notified when certain actions occur within the framework. 
Signals allow you to perform actions based on specific events, such as when an object is saved, deleted, or when a user logs in or logs out.

Heres an overview of how signals work in Django and some code samples to demonstrate their implementation:

Signal Definition:

Signals are typically defined in a signals.py file within your Django app.
You can use the django.dispatch.Signal class to define your custom signals.
Signals can be defined at the app level or project level, depending on your use case.
Signal Handlers:

Signal handlers are functions or methods that get executed when a signal is sent.
Signal handlers are connected to signals using the @receiver decorator or the Signal.connect() method.
Signal handlers can perform any custom logic or operations based on the received signal.
Here are some common examples of using signals in Django:

Example 1: Post-Save Signal


# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def mymodel_post_save(sender, instance, created, **kwargs):
    if created:
        # New object is created
        print("A new MyModel object was created!")
    else:
        # Existing object is updated
        print("An existing MyModel object was updated!")
In this example, the mymodel_post_save signal handler is connected to the post_save signal for the MyModel model. 
Whenever a MyModel object is saved, the signal handler is triggered. It checks the created parameter to determine if the object was created or updated.

Example 2: User Login Signal


# signals.py
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def user_login(sender, request, user, **kwargs):
    print("User", user.username, "logged in.")
    # Perform additional actions or logging here
In this example, the user_login signal handler is connected to the user_logged_in signal, which is sent when a user logs in.
The handler receives the sender (the User model), the request object, and the user who logged in.

To ensure that Django loads your signal handlers, you need to include an import statement in your app's apps.py file:

# apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals
Make sure to update your app's apps.py file and include the ready() method as shown above.

These examples demonstrate how to define signals and their associated signal handlers in Django. 
By using signals, you can decouple different parts of your application and respond to specific events with custom logic.













































....
