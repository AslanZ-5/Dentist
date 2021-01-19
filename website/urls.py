from django.urls.conf import path
from .views import home,contact
app_name = 'website'
urlpatterns = [
    path('',home,name='home'),
    path('contact/', contact, name='contact'),

]