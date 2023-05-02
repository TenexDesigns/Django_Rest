
Django has the Httpresponse and the HttpRequest to hand http request and responses. However the django restframwork hass the request and response 
objects which are more powerful and useful than those provided by django


django                                      django_restframwork
HttpRequest                                  request
HttpResponse                                 response


 DJANGO
 from django.shortcuts import render
from django.http import HttpResponse
  
  def product_list(request):
    return HttpResponse('ok')



REST FRAMWORK

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Respons

@api_view()
def product_list(request):
    return Response('ok')


















































































































...
