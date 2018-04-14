import xadmin
from .models import *
from apps.web_config import *
from xadmin.views import BaseAdminPlugin,CreateAdminView,ModelAdminView,UpdateAdminView


class UserAccountAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'nickname', 'user_acc', 'phone', 'email', 'log_time'
    ]
    # 将哪一列增加一个 点击可查询详细信息 的info图标
    show_detail_fields = ['user_acc']
    # 设置列表定时刷新
    refresh_times = (3,5)
    # 是否开启书签
    show_bookmarks = True
    # 设置要导出的文件的格式，可选格式：xls、xml、json
    list_export = ('xls','json')
    # 设置导出列
    list_export_fields = ('id', 'nickname', 'user_acc', 'phone', 'email', 'signature')

    # 设置只读
    def get_readonly_fields(self):
        '''
        这是定义只读字段的方法，限定普通用户对此字段仅拥有只读权限
        :param self:
        :return:
        '''
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields
    readonly_fields = ('user_pwd',)

class UserMessageAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    # 将哪一列增加一个 点击可查询详细信息 的info图标
    show_detail_fields = ['realname']
    # 设置列表定时刷新
    refresh_times = (3,5)

    list_display = [
        'realname', 'sex', 'birth', 'is_member', 'sf_code', 'face'
    ]

class UserStatusAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    # 将哪一列增加一个 点击可查询详细信息 的info图标
    show_detail_fields = ['acc_status']
    # 设置列表定时刷新
    refresh_times = (3,5)

    list_display = [
        'acc_status', 'is_marry', 'is_house', 'is_car', 'credit_status', 'is_business', 'is_real'
    ]

class UserMoneyAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    # 将哪一列增加一个 点击可查询详细信息 的info图标
    show_detail_fields = ['card_num']
    # 设置列表定时刷新
    refresh_times = (3,5)

    list_display = [
        'card_num', 'card_status', 'card_useful_money', 'card_ice_money', 'use_money_count'
    ]

xadmin.site.register(UserAccount, UserAccountAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserStatus, UserStatusAdmin)
xadmin.site.register(UserMoney, UserMoneyAdmin)


