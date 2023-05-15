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





3. REGESTERING NEW USERS

When we go to the users endpoint e.g



http::localhost/auth/users

    We can not send a get request to this end point with out authenticating first.
    However this endpoint has a Post request that is open to anonymous users, who can create an acount 
    So to regester a user , this end point sends a post reueest to that endpoint.
    The default form to be filled contains the email username and password.
    But what if we want to capture more information about the user like first name and last name
    To d that we will needd to go to djosers serliazer and customise it
    
    there are the default serilazers used by djoser to perform some operations, but using the settings module , we can easily relace this serialzer with our custom serializer
    DJOSER DEFAULT SERIALZERS FOR VARIOUS OPERATIONS
    {
    'activation': 'djoser.serializers.ActivationSerializer',
    'password_reset': 'djoser.serializers.SendEmailResetSerializer',
    'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
    'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
    'set_password': 'djoser.serializers.SetPasswordSerializer',
    'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
    'set_username': 'djoser.serializers.SetUsernameSerializer',
    'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
    'username_reset': 'djoser.serializers.SendEmailResetSerializer',
    'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',
    'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',
    'user_create': 'djoser.serializers.UserCreateSerializer',
    'user_create_password_retype': 'djoser.serializers.UserCreatePasswordRetypeSerializer',
    'user_delete': 'djoser.serializers.UserDeleteSerializer',
    'user': 'djoser.serializers.UserSerializer',
    'current_user': 'djoser.serializers.UserSerializer',
    'token': 'djoser.serializers.TokenSerializer',
    'token_create': 'djoser.serializers.TokenCreateSerializer',
}
    
    

TO CUSTOMISE OUR SERIALIZER OF DJOSE, WE CAN DO THAT IN OUR CORE APP OF THE PROJECT, SINCE THE CHANGES ARE REFLECTED ON THE ENTIRE APP

(1)we are customising this  'user_create': 'djoser.serializers.UserCreateSerializer', and so we customise it here below, and then we tell djoser to use the customised versuin in the settings,py file

#core App
serialzer.py


from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer   --> Here we give an alias to the User create


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):             ---> We inherit the implenation of theMeta class and just customise it to display our desired fields
        fields = ['id','username','password','email','first_name','last_name']

        
        
(2)  and then we tell djoser to use the customised versuin in the settings,py file      

#Project settings

settings.py





DJOSER ={
    'SERIALIZER':{
        'user_create':'core.serializer.UserCreateSerializer'              // Here we pass in our custome created USerCreateSeialazr to djoser by giving it the path to that  serialzer//We got user-ceate  from 'user_create': 'djoser.serializers.UserCreateSerializer', which was the default implenetaion of djoser
    }
}



LOGGING IN  OR AUTHENTICATING USERS


To Log in wee neeed an access token
We go to the link ending with this , e.g 

 We have thses three end poits for uthenticating users
 /jwt/create/ (JSON Web Token Authentication)   --> To create a new token, this is the logging endpoint
/jwt/refresh/ (JSON Web Token Authentication)
/jwt/verify/ (JSON Web Token Authentication)






ON GOING TO THIS END POINT AND LOGGGING IN WITH THE VALID CREDENTILAS, WE GET A REFRESH TOKEN , VALID FOR ONE DAYAND AND AN ACCESS TOKEN  VALID FOR 5 MINUTES
Access token is used fr accessing secure api end points , and the refresh token is used for getting a new accesss token when the access token expires
We can easily overide the lifespan of the access and refesh tokens  like here below in the settiings .py file of the project



Settings.py

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
}


THAT IS HOW LOGGING WORKS 


http::localhost/auth /jwt/create/   --> We go to this end point, log in usung valid credentilas and then get the access and refreshtokes , which we can store on the client

    TOKEN STOREGE IS DEFFERENT DEPENDING ON WHAT FRAMEOK YOU ARE USIG ON THE FRONT END
    FOR WEB APPS , WE USE JAVASCRIPT TO STORE TOKENS INSIDE THE BROWERES LOCAL STORAGE
    FOR MOBILE APPS TOKEN STOREAGE IS DIFFEENT BASED ON THE IMPLENETATION YOU ARE USING
    TO LOG OUT, ALL WE HAVE TO DO IS REMOVE THE TOKENS FROM THE LOCAL CLIENT ,NOTHING ELSE, THERE ARE NO END POINTS WE ARE GOING TO CALLL TO LOG OUT THEUSER



WAYS OF STORING THE JSON WEB TOKES




When it comes to storing tokens for accessing a web application, there are several common approaches you can consider:

Local Storage: You can store the token on the client-side using the browser's local storage or session storage. This approach allows the token to persist across browser sessions, but it is susceptible to cross-site scripting (XSS) attacks. To mitigate this risk, make sure to handle the storage securely and avoid storing sensitive information in the token.

Cookies: Another option is to store the token in an HTTP-only cookie. By setting the HttpOnly flag, you can prevent client-side scripts from accessing the cookie, thus reducing the risk of XSS attacks. Additionally, you can set the Secure flag to ensure the cookie is only sent over HTTPS.

Token in Authorization Header: Instead of storing the token directly, you can include it in the Authorization header of each request. This approach is typically used with the "Bearer" token scheme. The token is sent as Authorization: Bearer <token> in the request headers. With this method, you don't need to store the token explicitly, but you will need to send it with each request.

Server-Side Session: If you want to handle tokens on the server-side, you can store them in a session object or a database. Instead of relying on the client to present the token, the server associates the token with a user session on the server. This approach can be useful if you want more control over token management and revocation.

Token-based Storage Services: You can utilize token-based storage services, such as OAuth 2.0 providers like Auth0 or Firebase Authentication. These services handle token storage and management for you, allowing you to focus on integrating their authentication mechanisms into your application.

The choice of token storage mechanism depends on various factors such as the level of security required, the nature of your application, and your specific use case. Remember to consider the security implications and best practices for token storage, such as token expiration, revocation mechanisms, and secure transmission over HTTPS.





REFRESHING THE TOKEN

We can  us the refresh end point to refresh an get a neww access point it the access poit expires

e.g Refresh --> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MjI1NzQ1LCJpYXQiOjE2ODQxMzkyODcsImp0aSI6IjcyODJjNTNiMGQzMzQ5MWZiNTVmNGNjYjY5NzY2ODMxIiwidXNlcl9pZCI6MX0.tlD5DCfqLvZGXF0M9U1Bm6qVF5ps0-OIwKq_PgpDAY4
 then we will get a  new access token e.g access eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MjI1NzQ1LCJpYXQiOjE2ODQxMzkyODcsImp0aSI6IjcyODJjNTNiMGQzMzQ5MWZiNTVmNGNjYjY5NzY2ODMxIiwidXNlcl9pZCI6MX0.tlD5DCfqLvZGXF0M9U1Bm6qVF5ps0-OIwKq_PgpDAY4
  This new access token is valid for 5 mins by default but we can change the time in the settings.py file.

























































































































































....
