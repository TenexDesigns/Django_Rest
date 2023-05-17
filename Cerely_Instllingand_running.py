
INSTALLING CELLERY 

To use celery , you will first need a  message broker such as redis or rabbit mq

In this project we are going to be using redis
To use rdis , we first have to download it, to download it , we can use docker,
To use redis thriugh docker , first  we need to  download docker
Then run the follwing command in the terminal


docker run -d -p 6379:6379 redis


The first number 6378- Specifies where we want redis to be connect to our locla host, and the second number 6379 is the number redis communictaes with the local host
Redis runs in a container in docker an it communicates with our  local hsot app throught pot 6379

local host                               container
 port 6379                               redis -port 6379

  
  AFTER RUNING THE ABOVE COMMAND WE GET THIS CONFIMATION MESSSAGE THAT REDIS IS RUNNING
  tHE PORT OF THIS MESSAGE ASS 000.6379 TO SHOW US THAT THE LOCAL HOST IS COMMUNICATING WITH REDIS ON 6379/tcp
  
  CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                    NAMES
dbdefee787ec   redis     "docker-entrypoint.s…"   27 seconds ago   Up 24 seconds   0.0.0.0:6379->6379/tcp   hungry_mendeleev




  
  
  RUNNING TASKS IN THE BACKGROUND , in django USING  celery on windows
*****************************************************************************************************************************************

To run tasks in the background in a Django application using Celery on Windows, you can follow these steps:

1.Install Celery: Start by installing Celery using pip. Open a command prompt or terminal and run the following command:

    pip install celery


2.Configure Celery: Create a new file called celery.py in your Django project directory (the same directory where your settings.py file is located).
  Add the following content to the celery.py file:
    
 import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

    
    
    
3.Configure Django Settings: In your Django projects settings file (typically settings.py), add or modify the following settings:    
    # Celery Configuration
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'  # Replace with your broker URL
    
    
 4. Next : Go to the __url__.py file of the project folder  and add this so tha dkjnvo can know about the ceraly   
__init__.py File
   from .celery import app
    
  
                                       
CREATING AN D EXCUTING LONG RUNNING TASKS USING CELERY
  5.Create Tasks: Create a file called tasks.py in your Django app directory (the same directory where your models.py file is located). 
   Define your Celery tasks in this file. For example:
    
from time import sleep
from celery import shared_task                         //tHE TASK HERE IS TO PRINT THE LINES 


#This si how we define a task, now lets excute it
@shared_task                                                   //This is how we tell clery to excute this task
def notify_customers(message):
    print('Sending 10k emails ...')
    print(message)
    sleep(10)                                                  // this task is delayed for 10 secondss
    print('Emails were succesfully set !')

#To excute this, we need to decorate it with one of the celery decolartors

  
 
 6. Then we go to our view set to see and excute our task
 
 
from django.shortcuts import render
from .tasks import notify_customers


def say_hello(request):
    notify_customers.delay('Hello George Gacau')  // We call or excute the task by calling the delauy method on the task
    return render(request, 'hello.html', {'name': 'Mosh'})  // This will not be rendered untlll the task is completed after 10 seconds, but that does not happen becuse this task is being performned on a worker in cerely, that worker is different fom the process that is renduing our site

  
    
  5. Finally run the folliwng cimmand in the terminal  . This willl esure that the regetserdtasks will be given and discovered by celeray
  
         celery -A storefront worker --loglevel=info
   
celery -A [projectname]  [type of process we ant to strt(worker)] [and since we are testing and debugging (--logleve=info)]
The above should look something like this
    
    
    
   NOTE TAHT WE USE MESSAGGE BROKERS , BECUASE WE ARE ASSURED THAT THEY WILL DELIVER THE MESSAGES TO CLEERAY , EVEN IF CEREY IS TURNED OFF,
   tHEY WILL DELIVER AND EXCUTE THOSE TASKS OR MESSAGES IN CELERY WHEN CELERY IS TURNED BACK ON
   
   
    
    MORE EXPLANATION HERE BELOW
    **************************************************
    
       
    
    

import os
from celery import Celery  # Also import the celeary class

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

# set an enviroment module called django_setting_module, then specify the pathh to your settings module, and this refernces the settings module inside your projects folder


#Create a celery instance and give it an name within the brackets
app = Celery('storefront')
#Nest specify where you ca find the configuration variables
app.config_from_object('django.conf:settings', namespace='CELERY')
# this means we are going to go go to the module django.conf and load the settings object
#Next is a variable called namespace, and we set it to 'CELERY', meaning all our configuration settings should sattrt with cerela

# we ae going to create tasks  in the tasks.py file, and by callling this function, we are instrunftiong celeray to automaticlay find all of this tasks.
app.autodiscover_tasks()

# This is how we congigure celray, next we need to load this module inside the __init__ package of the project folder( the one containig the settings,py), because otherwise , python won't excute this code
# i.e in the  
__init__.py File
from .celery import Celery


## Finaly we need to start a celeay worker process by runnning th follwing command in the console


#celery -A [projectname]  [type of process we ant to strt(worker)] [and since we are testing and debugging (--logleve=info)]
# The above should look something like this
celery -A storefront worker --loglevel=info


RUNNING THE ABOVE COMMAND WILL GIVE US THE RESULT HERE BEOLOW

#  -------------- celery@DESKTOP-GTVINB0 v5.2.7 (dawn-chorus)
# --- ***** -----
# -- ******* ---- Windows-10-10.0.19045-SP0 2023-05-17 11:47:05
# - *** --- * ---
# - ** ---------- [config]
# - ** ---------- .> app:         storefront:0x18a4fff65c0
# - ** ---------- .> transport:   redis://localhost:6379/1
# - ** ---------- .> results:     disabled://
# - *** --- * --- .> concurrency: 4 (prefork)
# -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
# --- ***** -----
#  -------------- [queues]
#                 .> celery           exchange=celery(direct) key=celery


# [tasks]
#   . store.tasks.add

# [2023-05-17 11:47:06,931: INFO/MainProcess] Connected to redis://localhost:6379/1
# [2023-05-17 11:47:06,979: INFO/MainProcess] mingle: searching for neighbors
# [2023-05-17 11:47:08,085: INFO/SpawnPoolWorker-1] child process 14588 calling self.run()
# [2023-05-17 11:47:08,086: INFO/SpawnPoolWorker-2] child process 11100 calling self.run()
# [2023-05-17 11:47:08,208: INFO/MainProcess] mingle: all alone
# [2023-05-17 11:47:08,224: INFO/SpawnPoolWorker-4] child process 20324 calling self.run()
# [2023-05-17 11:47:08,483: INFO/SpawnPoolWorker-3] child process 1168 calling self.run()
# [2023-05-17 11:47:09,158: WARNING/MainProcess] D:\python\Django 3- Resources\Code\1- Getting Started\Start\storefront33\myworld\lib\site-packages\celery\fixups\django.py:203: UserWarning: Using settings.DEBUG leads to a memory
#             leak, never use this setting in production environments!
#   warnings.warn('''Using settings.DEBUG leads to a memory

# [2023-05-17 11:47:09,162: INFO/MainProcess] celery@DESKTOP-GTVINB0 ready.

This mean  that celeray is ready
also not that the above messga e stes that

warnings.warn(Using settings.DEBUG leads to a memory
It states this becuase currently we are in develepoment mode and debug is true, but i priduction. debug is false ,
              adnd we are not going to have that warning



In the above message we can see this text
- ** ---------- [config]
- ** ---------- .> app:         storefront:0x18a4fff65c0    -> This is the name of our celery app
- ** ---------- .> transport:   redis://localhost:6379/1    -> For transport , w have cerely connected to this redis instance
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)    --> $ infornt of concurency is the number of cpu core we are currently using,
              We have 4 crealy workers that are ready to pick up tasks
-- ******* ---- .> task events: OFF (en

 Ceraly is upp and running and nest we are going to see hoe to run tasks




    MORE EXPLANATION HERE BELOW
***************************************************************************************************************************8


To run tasks in the background in a Django application using Celery on Windows, you can follow these steps:

Install Celery: Start by installing Celery using pip. Open a command prompt or terminal and run the following command:

pip install celery
Configure Celery: Create a new file called celery.py in your Django project directory (the same directory where your manage.py file is located).
                                     Add the following content to the celery.py file:

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
Replace 'your_project_name' with the actual name of your Django project.

Configure Django Settings: In your Django project's settings file (typically settings.py), add or modify the following settings:

# Celery Configuration
CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'  # Replace with your broker URL
CELERY_RESULT_BACKEND = 'django-db'  # Use Django database as the result backend

# Celery Beat Configuration (Optional, for periodic tasks)
CELERY_BEAT_SCHEDULE = {
    'task_name': {
        'task': 'your_app.tasks.task_name',
        'schedule': 10,  # Task will run every 10 seconds
    },
}
Create Tasks: Create a file called tasks.py in your Django app directory (the same directory where your models.py file is located).
                                     Define your Celery tasks in this file. For example:

from celery import shared_task

@shared_task
def task_name():
    # Your task code here
    pass
Start Celery Worker: Open a command prompt or terminal and navigate to your Django project directory. Run the following command to start the Celery worker:

celery -A your_project_name worker --loglevel=info
Replace 'your_project_name' with the actual name of your Django project.

Run the Django Development Server: Open another command prompt or terminal, navigate to your Django project directory,
                                     and run the following command to start the Django development server:
Copy code
python manage.py runserver
Now, you should have Celery running in the background and ready to process tasks asynchronously.
                                     You can invoke the tasks from your Django views, models, or other parts of your application using the delay()
                                     method or by using the apply_async() method to specify task options.

Note: On Windows, you might need to install RabbitMQ or another message broker separately and configure it in your
                                     Django settings (CELERY_BROKER_URL) for Celery to work properly.

Remember to refer to the Celery documentation for more detailed configuration options and advanced usage: https://docs.celeryproject.org/en/stable/
























































































































