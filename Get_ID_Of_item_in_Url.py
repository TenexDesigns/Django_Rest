WE CAN GET THE ID OF THE ITEM FROM THE VIEWS FILE
 tHE VIEWS FILE HANDLES REQUEST THAT COME IN,
 
 IF WE ARE USING THE MODELVIEW SET IN OUR VIEWS , THIS IS HOW TO GET THE ID 
 
 
 
 
 
 class ProductList(ModelViewSet):
      serializer_class = ProductSerializer
      

      def get_queryset(self):
           return Product.objects.filter(collection_id = self.kwargs['collection_pk'])

      def get_serializer_context(self):
      #Remember that our url has two paramters, collection_pk and pk
           return {'collection_id':self.kwargs['collection_pk']}
           
     # self.kwargs - This is a dictionary that contains our url parameters



































