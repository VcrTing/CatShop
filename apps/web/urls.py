from django.urls import path
from web.views import *

app_name = 'web'
urlpatterns = [
    path('', to_index, name='to_index'),
]