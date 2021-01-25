from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('blog/',include('blog.urls')),
    path('appointments/',include('appointments.urls')),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView,name='logout'),
    path('register/', views.registerView, name='register'),
    path('password-reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete')





] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
