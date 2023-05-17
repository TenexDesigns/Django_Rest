RUNNING TASKS IN THE BACKGROUND USING CERALY

THERE ARE LONG RUNNING TASKS THAT TAKE TIME SUCH AS

-Processing images and videos
-Generating reports
-Sending emails
-Running machine learning models

THESE TASKS TAKE A LONG TIME AND WE DONT WANT THEM RUNNING ON THE PROCESS THAT RUNS OUR APPLICATION
BECAUSE IF THAT PROCESS IS BUSY , IT CANT CONTUNUE RESPONDING TO CLENT REQUESTS.
So we should keep the process1  running our app as free as posible and offload the long running tasks to another process2 or in other words, run it in the backrond


PROCESS 1                  PROCESS 2
                                    
APP                        Tasks taking time 





For example, when a user uploads a video, we dont want to make the user wait while we process the video,  We can process the video in the background and send a notification to the user after the vido has finished processsing , while th user is using other parts of our app.

HOW CAN WE DO THIS, WE CAN DO THIS , BY USING CELARY

USing celary , we can start several workers in the backroung

The application can send tasks throught the  queue. The wotksers await tasks from the queue



              task                 --->    worker1
Application   ---->      queue     --->    worker2
                                    -->    worker3


This means we can excute many tasks in parrel
If our system is overloaded , we can scale our system by adding more workers
This workers dont impact our main application process, so if a task is delayed or fails, it will not afffect our application process, and we can continue serving clients


With cerlely we can also schedule periodic tasks, e.g we can configure celary to run a task evey hour, or evey week or every day.




























































































...
