



5. Go to your vies file 
// The view.py
class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}             /// Here we send the productId to the serializer

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs['product_pk'])

// The serializer for the image

class ProductImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)  // Here we just set the id to the id sent from the url, the we just unpack the rest of the data

    class Meta:
        model = ProductImage
        fields = ['id', 'image']
