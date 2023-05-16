read more here --> https://github.com/adamchainz/django-cors-headers

Cross-Origin Resource Sharing (CORS) is a mechanism that allows web applications running on different domains to access each others resources. 
It is a security feature implemented by web browsers to prevent cross-site scripting attacks.

In Django, you can enable CORS by using the django-cors-headers package. Heres how you can set it up:

Step 1: Install the django-cors-headers package using pip:


pip install django-cors-headers
Step 2: Add corsheaders to your Django project's INSTALLED_APPS in the settings.py file:


INSTALLED_APPS = [
    # Other apps...
    'corsheaders',
]
Step 3: Add CorsMiddleware to the middleware classes in settings.py (preferably at the top):

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # Other middleware...
]
Step 4: Define the allowed origins in settings.py:


CORS_ALLOWED_ORIGINS = [
    'http://example.com',
    'https://example.com',
]
Replace example.com with the actual domain(s) from where you want to allow cross-origin requests. 
You can use the wildcard '*' to allow requests from any origin, but this is not recommended for production environments.





---------------------------

Configuration
Configure the middleware's behaviour in your Django settings. You must set at least one of three following settings:

CORS_ALLOWED_ORIGINS
CORS_ALLOWED_ORIGIN_REGEXES
CORS_ALLOW_ALL_ORIGINS





read more here ---->https://github.com/adamchainz/django-cors-headers






























































































































