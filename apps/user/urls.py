from django.urls import path,re_path
from .views import *

app_name = 'user'
urlpatterns = [
    # 注册
    path('register', RegisterView.as_view(), name='register'),

    # 登录
    path('login', LoginView.as_view(), name='login'),

    # 退出登录
    path('logout', LogoutView.as_view(), name='logout'),

    # 用户中心
    path('center', CenterView.as_view(), name='center'),

    # 忘记密码
    path('new_pwd', ForgetPwdView.as_view() , name='forgot_pwd'),

    # 获取资金
    path('get_mny', MoneyView.as_view(),name='get_user_money'),
]