1. SERIALIZER

TO GET CART ITEMS 

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']


        
        TO ADD CART ITEMS
        
    class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()                            // tHIS MEANS THAT THIS FIELD IS ADDED DYNAMICALY.i.E iT IS NOT IN THE DATABASE, SO WE HAVE TO ECIVE IT FROM THE USER. hERE WE SPECIFY WE WANT TO RECEIVE AN INTGER FIELD FROM THE USER

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No product with the given ID was found.')
        return value

    def save(self, **kwargs):                         // hERE WE OVERIDE THE SAVE METHOD , BECUSE WE WANT TO IMPLEMENT SOME CUSTOME CODE, SUCH AS JUST INCREASING THE QUANTY IDF A PRODUCT EXISTS 
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']              // tHIS DATA is useau validated in serilizer.is_valid() , then stored in serialix=zer.validated_data, but since we are in the  save function we can access the data throuth self.validate_data()     
        quantity = self.validated_data['quantity']

        try: 
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)   // hERE WE CHECKI IF THE CART ALREADY EXIST S USING THE CART ID, AND IF THAT CART HAS A  PRODUCT WE INCREASE THE QUANTUTIY OF THAT PRODUCT ONLY INSTEAD OF CREATING ANOTHER INSTANCE OF THAT PRODUCTAND INSTEDA OF CREATING A NEW ONE WE JUST INCREASE THE QUANTITY OF THE  EXISTING PRODUCT
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item                /// wE AHVE TO DO THIS WHEN WE OVERIDE THE SAVE METOD IN THE SERIALIZER, OR ANY OTHER METHODS IN THE SERIALIZER
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data) //hERE WE UNPACKE THE DATA RECEIVED FROM THE USER. wE USE THE CART ID TO ENSURE WE ARE CREATING AND UPACKING THE DATA TO THE RIGHT CART ITEM
        
        return self.instance   /// wE AHVE TO DO THIS WHEN WE OVERIDE THE SAVE METOD IN THE SERIALIZER, OR ANY OTHER METHODS IN THE SERIALIZER

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']
        
        
        
        
        TO UPDATE ONLY THE  QUANTITY OF THE CART ITEM
        
    class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
        
        

2. VIEW SET


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
   
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer                           // tHIS IS USED TO CREATE A NEW CATR ITEM
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer                        // tHIS IS USED TO UPFATDE THE QUANTTIY OF THE PRODYCT
        return CartItemSerializer                                         //// THIS IS USED TO GET THE CART ITEMS OF A GIVEN CART-ID

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}      // HERE W E PASS THE CART ID TO WHAT EVER SERIALIZER WE ARE USING, THIS ACRT ID IS USED IN THE ADDSERIALIZER

    def get_queryset(self):
        return CartItem.objects \
                .filter(cart_id=self.kwargs['cart_pk']) \           // THIS SIS WHERE WE GET THE CART_ID TO PASSS TO THE ADDSERILIZER THROUGH  THE CONTEXT METHOD.
                .select_related('product')





3.URLS

router.register('carts', views.CartViewSet)

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')




































































































...
