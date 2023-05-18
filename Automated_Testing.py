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
                                                                                       
                                                                                       






pip install --dev pytest-django 

We are going to install pytest as a development dependecy, So it is not a dependcy  that we neddd to deply with our application, for it to work


WRITTING OUR FIRST TEST

We go in  our app an create a  folder called tests.py  
We do this because it is what pytest loooks for, it looks for a folder names tetss in plural form
THe files we put in this folder should start with test_
e. text_collections.py To test the collections endpoint
    test_products.py to test the products end point



NOW TO WRITE THE TEST FUNCTION


The test functon should also start with test
It is also necessary to identitfy what  behaviour your test function is testing

e.g


e.g Here we are testing to see if a user is not authenticated , they will get a 401 error.


def test_if_user_is_anonymous_returns_401


WE ARE GOING TO PUT OUR TEST IN  ACLASS BASED O WHAT THEY DO

FOR EXAMPLE WE ARE GOING TO PUT THIS TESTS FOR THE COLLECTION END POINT IN A CLASS CALLED TESTCREATECOLLECTION, That is right, we should also start the class name with test, or else, pytest won't recodnize it

from rest_framwork.test import APIClient
from rest_framwork  import status
import pytest


@pytest.mark.django_db  # This is to give permissin to pytest to write to database
class TestCreateCollectiob:
  def test_if_user_is_anonymous_returns_401(self):
    #The test funtion cosnssite of three parts (AAA)
    #(ARRANGE, ACT, ASSERT)
   #ARRAGEN - wE PREPARE THE SYSTEM WE ARE GOING TO TEST, WE HWE PUT OUR objects or DATABASE IN AN INSTAIL STATE AND SO ON
  
  
  # Act - Where we  kick off the behaviour we want to test e.g This is where we send the request to  th server
  #To sent request  , we need to import the APIClient from rest_framwork.test
  client = APIClient()
  response = client.post('/store/collections/',{'title':'testing collections'})  #This is where we are going to send our requets, We also have to give it a title. When sending aresquest to the server, we gest a response.

  
  #Assertion - This is where we check if the bhaviour we expect , happens or not
  # In our above case we expect to get a 401 error form the server
  # Here we use the assert keyword
  # Here we check if the status is 401, for an unauthorused user
  asert response.status_code == status.HTTP_401_UNAUTHORISERD
  
  

  
  
  
  RUNNING TESTS
  *************************************************************************
To run our test we nned to tell pytest where our setings file is and for that we have to create a file  --> pytest.ini in the root folder i.e where the manage.py file is


pytest.ini

[pytest]

DJANGO_SETTINGS_MODULE = storefront.settings




and then you rn pytest in the console



TO TESTS  TESTS ONLY I N APRTICLUAR DIRECTORY
************************************************************************
You write pytest ad give the folder path to that test.
pytest store/tests

or a particlular file in you teste folder


pytest store/test/test_collection.py


or test a specific moule in the particluar file of the test folder


pytest store/test/test_collection.py::TestCreateColllection



we can also target a specific method


pytest store/test/test_collection.py::TestCreateColllection::test_if_user_is_anonymous_returns_401




We can also define a pattern , e.g Test only the test with anonymoius inside their name

pytest -k anonymous





TO TEMPORALY SKIP A TEST



@pytest.mark.django_db  
class TestCreateCollectiob:
  @pytest.mark.skip     /// We aplly this decolator to skip a test
  def test_if_user_is_anonymous_returns_401(self):
      client = APIClient()
      response = client.post('/store/collections/',{'title':'testing collections'})
      asert response.status_code == status.HTTP_401_UNAUTHORISERD





THERE ARE TWO WAYS TO RUN TESTS

There the o demand test, where we run our  test before commiting it to github or before  deploying it
Then there is the contionus testing that we do all the time   - This  is what is called contonous testing



FOR CONTIOUS TESTING WE HAVE TO INSTAL

pip install --dev pytest-watch





SO NOW INSTED OF RUNNING pytest  EVERY TIME WE WANT TO TEST OUR CODE
we run  ptw which stans for pytestwatch, and this will watch our code , for every change that w make.

ptw   
















































..
