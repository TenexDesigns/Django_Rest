
THIS IS USED TO PPLY PAGINATION ONLY TO ONE URL, THE PRODUCTS URL, TO APPLY THIS PAGGINATION TO ALL URLS, SEE BELOW


HERE WE USE THE GENINATION NUMBER , THAT WE SET IN THE SETTINGS FILE 

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING':False,
    'PAGE_SIZE':10
}





tHEN WE USE THE ABOVE PAGINATION NUMBER

from rest_framework.pagination import PageNumberPagination



class ProductList(ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
      filterset_class = ProductFilter
      search_fields = ['title','description']
      ordering_fields = ['unit_price','last_update']
      pagination_class = PageNumberPagination







TO APPLY PAGINATION TO ALL URLS 
*****************************************************************************************************************************************************
JUST WRITE THIS IN YOUR SETTINGS .PY FILE, AND ALL URLS WILL BE LIMITED TO TEN PAGES


REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING':False,
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10
}










HOW EVER IF WE USE EITHER OF THE ABOVE METHODS WE GET THIS ERROR


        HINT: The default for DEFAULT_PAGINATION_CLASS is None. In previous versions this was PageNumberPagination. 
    If you wish to define PAGE_SIZE globally whilst defining pagination_class on a per-view basis you may silence this check.
    
    

TO FIX THIS ERROR , LET US MAKE OUR OWN CUSTOM CLASS FOR PAGINATION
SO IN A NEW FILE IN THE APP



class DefaultPagination(PageNumberPagination):
      page_size = 10





THEN IN OUR VIEW FILE 



class ProductList(ModelViewSet):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
      filterset_class = ProductFilter
      search_fields = ['title','description']
      ordering_fields = ['unit_price','last_update']
      pagination_class = DefaultPagination





THEN IN OUR SETTINGS FILE




REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING':False,
 
}






WHEN YOU DO THIS, YOU CAN APPLU THIS PAGINATION ON YOUR DESIRED ROUTES


































































































...
