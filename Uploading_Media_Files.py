
HERE WE ARE GOING TO UPLOAD A USER FILE TO DJANGO AND DISPLAU  IT ON THE END POINT -> http://127.0.0.1:8000/media/car.jpg
    
    
    1. Go to your project and add a folder called media
    This will be the folder that will receive the user uploaded images
    In this folder we can add some images for example, a car image and a clowen image
    
    media/
         car.jpg
         crown.jg
    
    2.  Go to your projecs  settings.py file and add the follwing code
    
    import os
    
MEDIA_URL ='/media/'  #media_url -> refers to user uploaded files, # This is the end pont that we will receive our user uploaded files
                     
MEDIA_ROOT = os.path.join(BASE_DIR,'media')                      #Here we tell django where these media files are store in the django system
#BASE_DIR represnts the current working directory
# We then go to our urls file and define a path for serving this user uploaded files

  #  STATIC_URL = '/static/'  #Static_url ->Refers to static files like javascript, css images and os on. These are the files bundled with our application



  
  3. Go to your projects urls,puy file and add the folwung
  
  
from django.conf import settings          // Here we import the settings
from django.conf.urls.static import static
  
  urlpatterns = [
    path('admin/', admin.site.urls),
  ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                         //The url to be                    // The location where the store images or files are
                         used to upload or
                         display the images





4. Go to your models, where we want want to upload an image for a give product, so wecreate a many to one relationship between images and products because an product can have multiple images


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')  // This is used to establish the relationship between the products and the images
    image = models.ImageField(upload_to='images',)  // Here we specify the pathh where the uploaded mages are to be stores i.e In our project we declared a folder named mmedia, then the uploades images are to be uploaded in media in a file caleed images







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
















































































