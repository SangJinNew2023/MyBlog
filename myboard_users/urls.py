from django.urls import path
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
     path("login/", auth_view.LoginView.as_view(template_name='myboard_users/login.html', next_page='myboard:index'), name='login'),
     path("logout/", auth_view.LogoutView.as_view(next_page='login'), name='logout'),
     path("signup/", views.signup, name='signup'),

     #password reset
     path('password_reset/', views.password_reset_request, name='myboard_password_reset'),
     path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='myboard_users/password_reset_done.html'),
         name='myboard_password_reset_done'),
     path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='myboard_users/password_reset_confirm.html'),
         name='myboard_password_reset_confirm'),
     path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='myboard_users/password_reset_complete.html'),
         name='myboard_password_reset_complete'),
]