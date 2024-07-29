from django.urls import path
from . views import home,contact,about 

urlpatterns = [
    path('',home,name='home'),
    path('your-contact/',contact,name='contact-us'),
    path('about-us/',about,name='about-us')

   
]