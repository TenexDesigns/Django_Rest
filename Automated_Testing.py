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





TO TEST THE USER IS AN ADMIN OR NOT, WILL RECEIVE A 403 ERROR, meaning forbidden

from django.contrib.auth impost User

@pytest.mark.django_db  
class TestCreateCollectiob:
  def test_if_user_is_anonymous_returns_401(self):
      client = APIClient()
      response = client.post('/store/collections/',{'title':'testing collections'})
      asert response.status_code == status.HTTP_401_UNAUTHORISERD

  def test_if_user_is_not_admin_returns_403(self):
      client = APIClient()
      client.forceauthenticate(user={})   // This is how we authenticate
      response = client.post('/store/collections/',{'title':'user unauthoruse})
      asert response.status_code == status.HTTP_403_FORBIDDEN


  def test_if_user_is_data_is_invalid_returns_400(self):
      client = APIClient()
      client.forceauthenticate(user={User()is_staff=True})  
      response = client.post('/store/collections/',{'title':'})
                                                    
      asert response.status_code == status.HTTP_400_BAD_REQUEST
      assset respose.data[title] is not None    - This checkes if there is an error message.                                              


  def test_if_user_is_data_is_valid_returns_201(self):
      client = APIClient()
      client.forceauthenticate(user={User()is_staff=True})  
      response = client.post('/store/collections/',{'title':'vald user'})
                                                    
      asert response.status_code == status.HTTP_201_CREATED
      assset respose.data['ID'] > 0                                     





WE USE FIXTURES IN YTEST TO REMOVE DUPLICATION OOF CODE
***************************************************************************************************************************************
tO CRETE a fiture we nned to creat a file in the test fldder called conftest.py
                                                    
In our above test , w importted and created an instance of api_client in every test,
                                                    we can avoid tahy repetated importtion by using fixtures
                                                    
 from rest_framwork.test import APIClient
 import pytest
                                                    
  @pytest.fixture                                                  
  def api_client():
      return APIClient()                                               
                                                    
                                                    
  
                                                    
In our Test file, we import the api_client which return the APIClient() and use it
                                                    
                                                    
                                                    
  
from django.contrib.auth impost User

@pytest.mark.django_db  
class TestCreateCollectiob:
  def test_if_user_is_anonymous_returns_401(self,api_client):
      response = api_client.post('/store/collections/',{'title':'testing collections'})
      asert response.status_code == status.HTTP_401_UNAUTHORISERD
   
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
WHEN TESTING THE CRETE END POINT, WE NEED TO FILL THE REURED FIELD OF THE MODEL INSTANCE
TO DO THTAT WE USE A LIBARY CLAEED BAKER LIBARY THAT FILLS THE FIELDS WITH RANDM VALIES
 TO INSTALLL IT
                                                    
 pip install baker-libray
                                                    
                                                    
                                                    
                                                    
                                                    
@pytest.mark.django_db  # This is to give permissin to pytest to write to database
class TestCreateCollectiob:
  def test_if_user_is_anonymous_returns_401(self): 
#arranhe
collection = baker.make(Collection)      
                                                    
 ALSO PYTEST CRETES A MOCL DATABSE THAT IT DROPS AFTER WE FINISH OUR TESTING
                                                    
                                                    
                                                    
                                                    
    Automated testing in Django using pytest involves several steps, including installing the necessary packages, setting up the configuration files, and writing the test cases. In this answer, we will cover these steps and provide code samples for better understanding.

Install necessary packages:
To use pytest in Django, you will need to install the following packages:

$ pip install pytest
$ pip install pytest-django
$ pip install pytest-cov
pytest-django is a pytest plugin that provides tools for writing tests in Django, while pytest-cov is a plugin for measuring test coverage.

Set up configuration files:
First, create a test_settings.py file to override the necessary settings to be used while testing.

Next, create a pytest.ini file in your project root. This file tells pytest to follow certain rules before running:

[pytest]
DJANGO_SETTINGS_MODULE=test_settings
addopts = --nomigrations --cov=. --cov-report=html
Finally, create a .coveragerc file in your project root to specify which files or folders to omit in your tests.

Write tests:
Here is an example test case that checks if the create_user() function provided by Django is setting the username correctly:

import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_should_create_user_with_username() -> None:
    user = User.objects.create_user("Haki")
    assert user.username == "Haki"
In this example, we use the @pytest.mark.django_db decorator to allow database access for the test. To run the test and generate the coverage report, simply execute the py.test command in your terminal.

For more advanced usage, you can create fixtures for Django models and inject them into your test cases. Here is an example of creating a user fixture:

import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user_A():
    return User.objects.create_user("user_A")
To use this fixture in a test case, you can simply pass it as an argument:

def test_example(user_A):
    assert user_A.username == "user_A"
This allows you to reuse the fixture in multiple test cases and makes your tests easier to read and maintain realpython.com.

In conclusion, pytest simplifies the process of writing and running tests in Django projects. With the help of configuration files, fixtures, and decorators, you can create efficient and maintainable test suites for your Django applications.                                                
                                                    
                                                    
                                                    
                                                    MORE EXPLANTIOM
                                                    *************************************************************************************************************
                                                    
                                                    
                                                    
                                                    
Automated testing is an essential part of software development, and pytest is a popular testing framework that integrates well with Django. It provides a simple and expressive way to write tests for your Django projects. Let's walk through an example of writing tests using pytest in Django.

Setup:
First, ensure that you have pytest installed in your Django project. You can install it using pip:

Copy code
pip install pytest
Additionally, make sure you have a tests directory in your Django project, which is where we'll place our test files.

Writing a test case:
Let's say we have a Django app called myapp, and we want to test a model called Book. Create a new file called test_book.py inside the tests directory. Here's an example of a test case:

python
Copy code
# myapp/tests/test_book.py

import pytest
from myapp.models import Book

@pytest.mark.django_db
def test_book_creation():
    title = 'Test Book'
    author = 'John Doe'
    rating = 4.5

    book = Book.objects.create(title=title, author=author, rating=rating)
    assert book.title == title
    assert book.author == author
    assert book.rating == rating
In the example above, we import the Book model from myapp.models. The @pytest.mark.django_db decorator marks the test to use a database for testing, allowing us to perform database operations.

We define a test function called test_book_creation(). Inside the test function, we create a Book object with some test data. We then use assertions (assert) to check if the created book's attributes match the expected values.

Running the tests:
To run the tests, navigate to your project's root directory and execute the following command:

Copy code
pytest
pytest automatically discovers and runs all the tests located in the tests directory. You should see the test results in the console output.

Additional test cases:
You can write more test cases to cover different scenarios and edge cases. For example, let's add another test case to check the behavior of a method in the Book model:

python
Copy code
# myapp/tests/test_book.py

import pytest
from myapp.models import Book

@pytest.mark.django_db
def test_book_average_rating():
    book1 = Book.objects.create(title='Book 1', author='Author 1', rating=4.0)
    book2 = Book.objects.create(title='Book 2', author='Author 1', rating=4.5)
    book3 = Book.objects.create(title='Book 3', author='Author 1', rating=5.0)

    author_avg_rating = book1.author_average_rating()
    assert author_avg_rating == 4.5
In this test case, we create three books with the same author and different ratings. We then call the author_average_rating() method on one of the books and assert that the returned average rating matches the expected value.

By writing multiple test cases, you can ensure that your Django app's models, views, and other components are functioning correctly.

This is a basic example of how to write tests using pytest in Django. You can explore more advanced features of pytest, such as fixtures, parameterized tests, and test coverage reporting, to enhance your testing capabilities. Make sure to refer to the official pytest documentation (https://docs.pytest.org/) for detailed information and examples
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
