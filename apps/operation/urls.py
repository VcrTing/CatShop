from django.urls import path
from operation.views import *

app_name = 'operation'
urlpatterns = [
    path('order', my_order, name='my_order'),
    path('car', to_shopping_cat, name='to_shopping_cat'),
]