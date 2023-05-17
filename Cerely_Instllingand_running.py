
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




SCHEDULING PERIODIC WORKERS
******************************************************************************************************
 WE PUT THIS CODE IN THE SETTINGS.PY FILE

SCHEDULING PERIODIC TASKS IN CELERY
This good for doing tasks that are repedted after some time, such as after  every day, after every hour or month

This is important for Periodic tasks such as

Generating Periodic reports
Sending emails
Running mainatence jobs

For this scheduling of tasks we use celeray beat which is a task schedular
Celery beat
Celey beat is like a heart beat, it beats out a task after some time to be perormed by a celery worker
Celeray beat is a task schudular


Celery Beat Configuration (Optional, for periodic tasks)
CELERY_BEAT_SCHEDULE = {
    'notify_customers': {
        'task': 'playground.tasks.notify_customers',
        'schedule': 10,  # Task will run every 10 seconds
    },
}

To start the celery beat process

celery -A storefront beat
We start the beat process with this commant
    Preveious we had satrteda worker process, but here we want to start a beat proccess


celery -A storefront worker --loglevel=info




IF YOU WANT THE TIME TO BE IN MIMUTES


'schedule': 10* 60


How ever if you want more cobtrov ob=ver tha time  the use ths crontab objec from celeay

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'notify_customers': {
        'task': 'playground.tasks.notify_customers',
        'schedule': crontab(day_of_week=1,hour=7,minute=30),  # Task will run every 10 seconds
        'args':['Hello George Gacau] -> We use this if there are any arguments needed by the task  
         'kwargs':{} ,   --> It also   accepts key word arguments

},    
}

The scdule
'schedule': crontab(day_of_week=1,hour=7,minute=30),

Means to excute the above stated task every first day of week(monday ) on 7:30



This means that the task should be excuted evry 15 muinutes
'schedule': crontab(minute='*/17'),

HERE ARE OTHER EXAMPLES OF USING CONTRIB

Example

Meaning

crontab()

Execute every minute.

crontab(minute=0, hour=0)

Execute daily at midnight.

crontab(minute=0, hour='*/3')

Execute every three hours: midnight, 3am, 6am, 9am, noon, 3pm, 6pm, 9pm.

crontab(minute=0,
hour='0,3,6,9,12,15,18,21')

Same as previous.

crontab(minute='*/15')

Execute every 15 minutes.

crontab(day_of_week='sunday')

Execute every minute (!) at Sundays.

crontab(minute='*',
hour='*', day_of_week='sun')

Same as previous.

crontab(minute='*/10',
hour='3,17,22', day_of_week='thu,fri')

Execute every ten minutes, but only between 3-4 am, 5-6 pm, and 10-11 pm on Thursdays or Fridays.

crontab(minute=0, hour='*/2,*/3')

Execute every even hour, and every hour divisible by three. This means: at every hour except: 1am, 5am, 7am, 11am, 1pm, 5pm, 7pm, 11pm

crontab(minute=0, hour='*/5')

Execute hour divisible by 5. This means that it is triggered at 3pm, not 5pm (since 3pm equals the 24-hour clock value of “15”, which is divisible by 5).

crontab(minute=0, hour='*/3,8-17')

Execute every hour divisible by 3, and every hour during office hours (8am-5pm).

crontab(0, 0, day_of_month='2')

Execute on the second day of every month.

crontab(0, 0,
day_of_month='2-30/2')

Execute on every even numbered day.

crontab(0, 0,
day_of_month='1-7,15-21')

Execute on the first and third weeks of the month.

crontab(0, 0, day_of_month='11',
month_of_year='5')

Execute on the eleventh of May every year.

crontab(0, 0,
month_of_year='*/3')

Execute every day on the first month of every quarter.
MORE DOCUMENTATION

Crontab schedule.

A Crontab can be used as the run_every value of a periodic task entry to add crontab(5)-like scheduling.

Like a cron(5)-job, you can specify units of time of when you’d like the task to execute. It’s a reasonably complete implementation of cron’s features, so it should provide a fair degree of scheduling needs.

You can specify a minute, an hour, a day of the week, a day of the month, and/or a month in the year in any of the following formats:

minute
A (list of) integers from 0-59 that represent the minutes of an hour of when execution should occur; or

A string representing a Crontab pattern. This may get pretty advanced, like minute='*/15' (for every quarter) or minute='1,13,30-45,50-59/2'.

hour
A (list of) integers from 0-23 that represent the hours of a day of when execution should occur; or

A string representing a Crontab pattern. This may get pretty advanced, like hour='*/3' (for every three hours) or hour='0,8-17/2' (at midnight, and every two hours during office hours).

day_of_week
A (list of) integers from 0-6, where Sunday = 0 and Saturday = 6, that represent the days of a week that execution should occur.

A string representing a Crontab pattern. This may get pretty advanced, like day_of_week='mon-fri' (for weekdays only). (Beware that day_of_week='*/2' does not literally mean ‘every two days’, but ‘every day that is divisible by two’!)

day_of_month
A (list of) integers from 1-31 that represents the days of the month that execution should occur.

A string representing a Crontab pattern. This may get pretty advanced, such as day_of_month='2-30/2' (for every even numbered day) or day_of_month='1-7,15-21' (for the first and third weeks of the month).

month_of_year
A (list of) integers from 1-12 that represents the months of the year during which execution can occur.

A string representing a Crontab pattern. This may get pretty advanced, such as month_of_year='*/3' (for the first month of every quarter) or month_of_year='2-12/2' (for every even numbered month).

nowfun
Function returning the current date and time (datetime).

app
The Celery app instance.

It’s important to realize that any day on which execution should occur must be represented by entries in all three of the day and month attributes. For example, if day_of_week is 0 and day_of_month is every seventh day, only months that begin on Sunday and are also in the month_of_year attribute will have execution events. Or, day_of_week is 1 and day_of_month is ‘1-7,15-21’ means every first and third Monday of every month present in month_of_year.

is_due(last_run_at)[source]
Return tuple of (is_due, next_time_to_run).








MONITORING CELERY TASKS
******************************************************************************************

                
                tO DO THIS ,  W USE A TOOL CLAAED FLOWER
                
                1. pip install flower
                
                2.  celery -A storefront flower
                This is to start flower, and we can access it on localhost:5555
                In the site, we can see the active workers, the state of th workers and the runtime and may more








































































































