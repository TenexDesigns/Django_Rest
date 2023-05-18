




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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





