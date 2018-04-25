from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('q_result', QueryResultView.as_view(), name='query_result'),
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),
    path('item/<int:item_id>', ItemView.as_view(), name='item'),

    path('add_cart', AddCartView.as_view(), name='add_cart'),
    path('car/<int:item>', ShoppingCatView.as_view(), name='shopping_cat'),
]