from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.blogView,name='blog'),
    path('art-create/', views.createView, name='art_create'),
    path('detail/<int:pk>/', views.detailView, name='detail'),

]