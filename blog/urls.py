from django.urls import path
from . import views
from . views import updateView,deleteView
app_name = 'blog'
urlpatterns = [
    path('', views.blogView,name='blog'),
    path('detail/<int:pk>/', views.detailView, name='detail'),
    path('art-create/', views.createView, name='art_create'),
    path('detail/<int:pk>/update/',updateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/',deleteView.as_view(), name='delete'),

]