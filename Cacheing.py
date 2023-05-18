
CACHEING  -- > This is a perfromace optimisatio  technique



cache backedns

local meemrut - default - good for development but bad fro production
memecached
Database
File system
Redis   -- All the above come with django, but redis comes in a separate libray




INSTALLING REDIS
tO RUN REDIS WE USE docker

----> docker  run -d -p 6379:6379 redis



To use redis as a cache in a django application, we should install djnago redis

pip install django-redis



To start using django-redis, you should change your Django cache settings to something like:
  
setting.py
  
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}




USING LOW LEVEL CACHE API

from django.core.cache import cache     // this cache object has an api for accesing the cache. It has method for getting objects from the cache or storing them in the cache


def say_hello(request):
  key = 'httttp_result'
  if cache.get(key) is None:  //Here we check if there is any data in our cache, and if there is none , we get it and save it in our cache
    response = request.get('https:httpbin.org/delay/2')
    data = response.json()
    cache.set(key,data,10*60)// We can set the time out fr the cache ,e. 10 *60
  return render(request,'hellow.html',{'name':cach.get(key)})  




or set the time out globaly
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
         'TIMEOUT':10 *60
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}



WE CAN ALSO DO CACHING USING OUR DECOLARTOR  TAT HANDLES ALL THE ABOVE LOGIC AND ISES LESS CODE
*****************************************************************************************************************
// Here django takes care of the low leve complaxity


from django.views.decorators.cache import cache_page


@cache_page(5 * 60)  / This decolator works on finction based views
def say_hello(request):
  response = request.get('https:://httpbin.org/delay/2')
  data = response.json()
  return render(request, 'hello.html',{'name':data})







FOR CLASS BASED VIEW
we have to wrap cache_page inside aotjher decolator called method_decolator 


from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': data})






*********************************************************************************************************************************88


















