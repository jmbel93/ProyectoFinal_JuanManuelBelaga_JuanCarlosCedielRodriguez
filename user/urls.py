from django.urls import path

from user import views
from user.views import *



app_name='user'
urlpatterns = [
    path('login/', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('signup', views.register, name='user-register'),
    path('profile', views.user_update, name='user-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
]
