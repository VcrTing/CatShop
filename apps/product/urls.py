from django.urls import path
from product.views import *

app_name = 'product'
urlpatterns = [
    path('q_result', query_result, name='query_result'),
    path('category', category, name='category'),
    path('item', item, name='item'),
]