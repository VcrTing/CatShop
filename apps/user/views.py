from django.shortcuts import render

# Create your views here.
def to_center(request):
    '''
    跳转至用户个人中心界面
    :param request:
    :return: user_center.html
    '''
    return render(request,'user_center.html')

def to_register(request):
    '''
    去登录界面
    :param request:
    :return:register.html
    '''
    return render(request, 'user_register.html')

def register(request):
    '''
    用户注册逻辑
    :param request:
    :return: user_center.html
    '''
    return render(request, 'index.html')

def to_login(request):
    '''
    去找回密码的界面
    :param request:
    :return: index.html
    '''
    return render(request, 'user_login.html')

def to_forgot_pwd(request):
    '''
    去找回密码的界面
    :param request:
    :return:
    '''
    return render(request, 'index.html')

def login(request):
    '''
    用户登录逻辑,及其页面返回
    :param request:
    :return:
    '''
    return render(request, 'index.html')

def logout(request):
    '''
    退出登录
    :param request:
    :return:
    '''
    return render(request, 'index.html')