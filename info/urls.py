from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('profile',views.home,name ="home"),
    path('logout',views.logout,name="out"),
    path('login',views.login,name="in"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('reset',views.reset,name="forgot"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "reset_password.html"),name = "reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_done.html"),name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "reset_complete.html"),name="password_reset_complete"),
    
    
     
        
]
