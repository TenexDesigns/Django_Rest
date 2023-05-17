WITH AUTOMATED TESTING , YOU CAN WRITE CODE TO TEST YOUR CODE
tO TEST your api endpoints and their bussines rule

So we write this code once and run it over and over, when we change our software or when we deploy it.  


TEST BEHAVIOUR  AND NOT IMPLEMETTION


You have alredsy  wriiiten the code for your endpoints, now all you need to test is if these endpoints work correbctly ass expected  and no their implementation
So test how an api behaves and not how it is implemetetd , since implemantion can change i.e  hwo some code  is writen can change

TESTING THE BEHAVE OF AN ENDPOINT


E,G post/collections


Anonymous -> 401  Unauthorised
Non-admin -> 403  Forbidden
Admin && Invalid data -> 400  Bad request
Admin && valid data -> 200  ok 

We can test this behaviour manualy on the browser or automate it with code



TEST FRAMWORKS

We nned a framwork for wrinting tests

A test framwork gives us a structure for writting tests as well as a program to run our tests and give us a report 



TEST FROAMWORKS INCLIDE
Unittest - Which comes with python
pytest - Which we have to install separately. Py test is a better framwork because it ---> Has more features
                                                                                      ---> Tons of plugins 
                                                                                      ---> less boilerplate code 
                                                                                       
                                                                                       






pip instal --dev pytest 

We are going to install pytest as a development dependecy, So it is not a dependcy  that we neddd to deply with our application, for it to work
































































































..
