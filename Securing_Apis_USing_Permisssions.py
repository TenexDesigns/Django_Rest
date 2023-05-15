Here we are Going to discuss how to secure api endpoints using permissions

1. Token-based authentication
2.Adding authentication end points
3. Registering , logging in and e.t.c
4. Applying Permissions




1. Token-based authentication

Token-based authentication in Django is a method of authentication that uses tokens to verify and grant access to resources or APIs.
It is commonly used for stateless authentication in web applications and allows clients to authenticate themselves with 
a token instead of sending their credentials with each request.

Heres how token-based authentication typically works in Django:

User Registration:
  Users register and create an account by providing their credentials (e.g., username and password).

Token Generation:
  Once the user is registered and authenticated, a token is generated for that user. This token contains encoded information about the user and is associated with their account.

Token Storage: 
  The generated token is then securely stored on the client-side, usually in local storage or a cookie. This allows the client to include the token with each subsequent request.

Token Submission:
  When the client wants to access a protected resource or API endpoint, it includes the token in the request headers, typically using the "Authorization" header with the "Bearer" scheme. For example: Authorization: Bearer <token>

Token Verification:
  In Django, a middleware or decorator intercepts the incoming request and extracts the token from the header. It then verifies the authenticity of the token, checking if it has been tampered with or expired.

User Authentication:
  If the token is valid, Django identifies the user associated with the token and considers the user authenticated for that request. The user's information can then be accessed throughout the request cycle.

Access Control:
  Once authenticated, Django can enforce access control rules to determine if the user has permission to perform the requested action on the resource or API endpoint.

Token Expiration and Refresh: 
  To enhance security, tokens usually have an expiration time. When a token expires, the client can request a new token by providing their refresh token (if implemented) or by re-authenticating with their credentials.

Token Revocation: 
  In case a token is compromised or a user logs out, it is essential to have a mechanism to revoke tokens. This can be implemented by maintaining a blacklist of revoked tokens or by using short-lived tokens with frequent renewals.

Django provides built-in support for token-based authentication through the Django REST Framework (DRF). DRF offers utilities and views for token authentication, making it easier to implement token-based authentication in Django web applications.

Remember, token-based authentication should be used over a secure (HTTPS) connection to prevent token interception and unauthorized access.











2.Adding authentication end points

Django  comes with a full fledged authentication system, but this system does not include an api layer, so we don t have any end points for users to register  logginand so on
We only have a bucnh of models and database tables in the authenication system
We can buuld this api layer by hand, but that is pretty tedeous and repettive, and we dont want to repeat that in every project
This is where we use Djoser, Djoser is a restful implementation of the django authentication system .
Djoser provides a bunch of views for registration, login, logout, password reset and so on


Thses are the endpoints that djoser add to our project backend

/users/                          ---> For managing users
/users/me/                          --->  For getting the current user
/users/confirm/
/users/resend_activation/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/
/token/login/ (Token Based Authentication)
/token/logout/ (Token Based Authentication)
/jwt/create/ (JSON Web Token Authentication)
/jwt/refresh/ (JSON Web Token Authentication)
/jwt/verify/ (JSON Web Token Authentication)



(1)TO INSTALL DJOSER

$ pip install -U djoser

(2)CONFIGURE DJOSER IN THE  SETTINGS.PY FILE OF THE PROJECT

INSTALLED_APPS = (
    'django.contrib.auth',
    'rest_framework',
    'djoser',
)

(3)IN THE URLS.PY FILE OOF THE PROJECT

urlpatterns = [
    url('auth/', include('djoser.urls')),                     -- All the url endponts provided by djoser have been deligated here, so they will all start as e.g auth/user    or authuser/me
]



DJOSER RELIIES ON AN AUTHENTICATION ENGINE TO DO THE ACTUAL AUTHENTICATION,BECAUSE DJOSER IS JUST A API LAYER, WITH VIES SERIALIZER AND ROUTES
SO WE NNED AN ACTUAL AUTHENTICATION ENGINE TO DO THE ACTUAL WORK

AUTH ENGINES

Token-based authentication  - Is built in django rest frame-work. USes a database table to store tokens. So fir everuy request, a database call is nneded 
JSon web token authentication - Doesnt need a databsae or a database call. Every token has a signature and on the server we can ensure that the the token is valid


HERE WE ARE GOING TO USE JSON WEB TOKEN 

(1)If you are going to use JWT authentication, you will also need to install djangorestframework_simplejwt with:

$ pip install -U djangorestframework_simplejwt

(2)Add rest_framework_simplejwt.authentication.JWTAuthentication to Django REST Framework authentication sIn the settings.py file of the project
settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

(3) Add this after the Rest_Framwork adove in the Projects settings,py file

Configure django-rest-framework-simplejwt to use the Authorization: JWT <access_token> header:
settings.py
    
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),      // This sepecifies the prefix that should be included in the request header.So for sending the authentiction token to the server, we are going to prefix the token with jwt
}


(4) We need to include one more url in the main projects url file
urls.py

urlpatterns = [
    (...),
    url('auth/', include('djoser.urls')),
    url('auth/', include('djoser.urls.jwt')),
]





















































....
