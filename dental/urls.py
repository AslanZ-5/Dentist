from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView,name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
