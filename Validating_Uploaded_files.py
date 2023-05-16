

file called validators.py



from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 500

    if file.size > max_size_kb * 1024:
        raise ValidationError(f'Files cannot be larger than {max_size_kb}KB!')

        
        
        file in models.py 
        
        
        class ProductImage(models.Model):
        product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
         image = models.ImageField(upload_to='store/images',validators=[validate_file_size])





















































