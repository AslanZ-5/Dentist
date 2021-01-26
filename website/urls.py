from django.urls.conf import path
from .views import home,contact,about,price,sendMessage
app_name = 'website'
urlpatterns = [
    path('',home,name='home'),
    path('contact/', contact, name='contact'),
    path('about/',about, name='about'),
    path('price/',price, name='price'),
    path('send-message/',sendMessage, name='send-message')


]