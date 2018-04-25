from django.urls import path
from .views import *

app_name = 'web'
urlpatterns = [
    path('', IndexView.as_view(), name='to_index'),
]