




Run performance tests while building an application
With performance testing we can identitfy and fix perofrmance problems


We can performace our django application with locust

pip install --dev locust


We have to find core use cases , or funtions esentioal for our bussinesfor our app

e.g

Core Use cases
-> Browse products
-> Register sign in , sign out


Then we create a test script for each use case, sepecifiying the action a user will take

Go to your root folder and create a new folder -> locastfiles
Inside this folder create a file to teste you use cases

e.g browe_products.py


from locust import HttpUser, task, between
from random import randint
#LOcast will excuete the tasks we deine here for each us
#rasks such as viewing produtcs
#viewing product details
#Adding products to cart
#fro each task, we deine a separate method
class WebsiteUser(HttpUser):  # This class must extedn the HttpUser class
  wait_time = between(1, 5)  // Locast will wait , between 1-5 secionds between each task , becuase users cam wait between 1-5 seconds to perform a statsk

  @task
  def view_products(self):
    collection_id = randint(2,6) 
    self.client.get('/store/produts/?collection_id',name='/store/products/')

  @task
  def view_product(self):
    product_id  range(1,1000)
    self.client.get(f'/store/products/{product_id}',name='/store/products/:id')

    
    @task(2)    // We can give tasks a weihght, meaning how often it is performed
    def view_products(self):
      product_id = range(1,10)
      self.client.post(
      f'/store/carts/{self.cart_id}/items/',name ='/store/carts/items/'
        json={'product_id':product_id,'quantitiy':1}
      )


      
      def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.jsom()
        self.cart_id = result['id']
    
    
    RUNNING LOCUST TEST FILES FOR TESTING PEROFMANCE
    locust -f locustfiles/brose_products.py
    
    
    After running this, a new site will be opppned on 
    http://0.0.0.0:8089/
        ,You will have to specify number of users on peack performce, your site uer, and the number of users you want to be added per second
    
    This site will display the follwing 
    
    
    
    
    Type     Name                # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s--------|------------------|-------|-------------|-------|-------|-------|-------|--------|-------------------|------------------|-------|-------------|-------|-------|-------|-------|--------|-----------         Aggregated               0     0(0.00%) |      0       0       0      0 |    0.00        0.00
Response time percentiles (approximated)
Type     Name                        50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|----------------------|--------|------|------|------|------|------|------|------|------|------|------|------
--------|----------------------|--------|------|------|------|------|------|------|------|------|------|------|------
    
    
    
    THE PERFORMANCE TEST WRITTEN IN LOCUST USING PYTIN
    **************************************************************************************************************************************
    
    
    
    
    
    from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
  wait_time = between(1, 5)

  @task(2)   // tHE task decorator is to tell locust to excute tis, the two is simply a priority umber, the higher the number the hiher or the more likely a task is to be performed by a user
  def view_products(self):
    collection_id = randint(2, 6)        // There are about 6 collection sin our database, and the 100 products are in one of theses 6 colections, we give the collection a random id between 2 and 6 so tat the user can view products from differen t collections
    self.client.get(
      f'/store/products/?collection_id={collection_id}', 
      name='/store/products')  // This is  ag group name for all the teste do on the above end point , this will give us the performance of this end point  under this gtroup name


  @task(4)
  def view_product(self):
    product_id = randint(1, 1000)
    self.client.get(
      f'/store/products/{product_id}',
      name='/store/products/:id')

  @task(1)
  def add_to_cart(self):
    product_id = randint(1, 10)
    self.client.post(
      f'/store/carts/{self.cart_id}/items/',
      name='/store/carts/items',
      json={'product_id': product_id, 'quantity': 1}
    )

  def on_start(self):
    response = self.client.post('/store/carts/')
    result = response.json()
    self.cart_id = result['id']
    
    
    
    
    By doing perfromance testin , we can identitfy a few of the slow ed points
    Now let us discuss optimisation techniques
    90% of the time the isssue is the qurery or in the database
    
    
    
    OPTIMISATIONS
    Optimise the python code- We have to ensure that our python code does not translate to costly querys, we can do that in hte followin wau
    Re-write the qury , if the query is slow, and django orm is not doing a good job of generationg fast ssql qury
    Tune the database  by redsesingning our tables. adding indexes and so on.
    Cache the result - Store the result in memeory
    
    1. Preload realted objects
    Products.objects.select_related('...')
    Products.objects.prefetch_related('...')
    
    2.Load only what you need
    Product.objects.only('title')         /// Load only the tile field
    Product.objects.defer('descritpion')  // Do not load the description, incase it has a lot of data with it, we can come for it later
    
    3. Use values
    Products.objects.values()  // We get a dictonary
    Products.objects.values_list()  // We get a list    // Intializing a django list or dictionary is cheaper that instializing a model. If you don;t need any of the behabiours of a django model like creating, updationg or deleting, then you can use one of these methods
    
    4.Count propery
    Products.objects.count()   // If you want to count product , this is the right way to do it
    len(Product.object.all())   // Wrong way to do it, as this is super expensive
    
    
    5.Bulk create or update- Bulk creating or updationg, if you want to create or update multiple objects, then it is better and more efficient to use bulk create, than updating  bunch of objects in a loop, because we send one instrunction to the database to create mutiple objects
    Products.objets.bulk_create([])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





