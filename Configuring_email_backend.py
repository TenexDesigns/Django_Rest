
COMFIGUTITNG EMAIL BACKEND

An email backend is an engine that is responsible for sending emails

EMAI BACKENDS IN DJANGO

Smtp(default)   - Uses an smpt server to send emails
Console backend    - The emails we send will appear in the console or terminal window
File  - Backend for writting emails to a file
Locmem  --> for writting emails to  Local memeory
Dummy backend - that does nthing



TO SET E.G THE CONSOLE BACKEND , WE GO TO THE SETTINGS .PY OF OUR PROJECT


settings,py


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'   - SMPT
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  - -CONSOLE
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'  - FILE BASED



IN OUR PROJECT WE ARE GOING TO USE THE SMPT BASED BACKEND
THIS IS HOW WE CONFIGURE OUR EMAIL BACKEND

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'localhost' --> Because this is where we are running our smpt server
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD =''
EMAIL_PORT =2525
DEFAULT_FROM_EMAIL ='munyambu6537@gmail.com'



HOW TO SEND EMAILS
 
TO SEND EMAILS , WE CAN Go TO OUR VIEW SET AND SEND AN EMAIL WHEN A VIEW ST IS CALLED


there are several methods for sending mails
send_mass_mail - Use this to send mails to more than one user, or to send bulk emails or to sned many emails. Use this ne at all times
send_mail - Use this to send emails to one user at a time
mail_admins - We use this one to send emails to all admins

from django.core.mail import mail_admins,mail_managers,send_mail,send_mass_mail
from django.shortcuts import render


def say_hello(request):
  send_mail('subject','message','sendingemail',['list of recepients of this email'])
    return render(request, 'hello.html', {'name': 'Mosh'})



Now you should always wrap the semad mail in a try block and send a BadHeader error incasee an atter trys to intercept the email and send a fake email to your client , so ur email will look somethoing like this


from django.core.mail import mail_admins,mail_managers,send_mail,send_mass_mail
from django.shortcuts import rende

def say_hello(request):
  send_mail('subject','message','gacau@gmail.com',['george@gmail.com'])
    return render(request, 'hello.html', {'name': 'Mosh'})











