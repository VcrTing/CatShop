from django.urls import path
from user.views import *

app_name = 'user'
urlpatterns = [
    path('login', login, name='login'),
    path('loginout', logout, name='logout'),
    path('register', register, name='register'),
    path('center', to_center, name='to_center'),
    path('to_login', to_login, name='to_login'),
    path('fpwd', to_forgot_pwd, name='to_forgot_pwd'),
    path('to_register', to_register, name='to_register'),
]