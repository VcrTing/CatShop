from django.urls import path
from user.views import *

app_name = 'user'
urlpatterns = [
    path('center', to_index, name='to-index'),
]