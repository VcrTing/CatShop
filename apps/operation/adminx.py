import xadmin
from .models import *
from apps.web_config import *

site_title = WEB_SITE_TITLE
site_footer = WEB_SITE_FOOTER

class OrderAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    # 将哪一列增加一个 点击可查询详细信息 的info图标
    show_detail_fields = ['order_code']
    # 设置列表定时刷新
    refresh_times = (3,10)

    list_display = [
        'order_code', 'receiver', 'mobile', 'user_msg',
         'delivery_time', 'status', 'pay_time', 'data_status'
    ]

class OrderItemAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    # 将哪一列增加一个 点击可查询详细信息 的info图标
    show_detail_fields = ['product']
    # 设置列表定时刷新
    refresh_times = (3,10)

    list_display = [
        'product', 'order', 'user_account', 'status', 'create_time', 'data_status'
    ]

xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(OrderItem, OrderItemAdmin)