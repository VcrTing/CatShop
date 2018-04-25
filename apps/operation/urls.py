from django.urls import path
from apps.operation.views import *

app_name = 'operation'
urlpatterns = [
    path('buy_one', BuyOneView.as_view(), name='buy_one'),
    path('buy', BuyView.as_view(), name='buy'),
    path('go_pay', GoPayView.as_view(), name='go_pay'),
    path('payss', PayedView.as_view(), name='payed_success'),
    path('order', MyOrderView.as_view(), name='user_order'),
    path('settlement', SettlementView.as_view(), name='settlement'),
    path('get_goods', GetGoodsView.as_view(), name='get_goods'),
    path('got_goods', GotGoodsView.as_view(), name='got_goods'),

]