from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponsePermanentRedirect,HttpResponse,JsonResponse
from django.urls import reverse
from django.db.models import Q
from .forms import *
from .models import *
from apps.web_config import *
from django.forms.models import model_to_dict
from django.db import transaction

# Create your views here.
# setting中需要有对应的配置
# 将用户权限提升为web后台管理员
# setting中需要有对应的配置 => AUTH_USER_MODEL = 'user.UserAccount'
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserAccount.objects.get(Q(nickname=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 注册逻辑的实现
class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, "user_register.html", {'register_form': register_form, 'error':''})

    @transaction.atomic
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            # 判断是否存在此用户
            check_user = UserAccount.objects.filter(email = email)
            if check_user:
                return render(request, 'user_register.html', {'error':'用户已经存在！可去登录哦～'})
            # 用户生成
            user_account = UserAccount()
            user_account.email = email
            user_account.nickname = email
            user_account.create_time = datetime.datetime.now()
            user_account.phone = STR_NUM_DEFAULT
            user_account.user_pwd = password
            user_account.save()
            # 资料信息生成
            user_message = UserMessage()
            user_message.nickname = email
            # 状态信息生成
            user_status = UserStatus()
            # 用户账户生成
            user_money = UserMoneyCount()

            user_account = UserAccount.objects.get(Q(email=email) & Q(user_pwd=password))

            user_message.user_account = user_account
            user_message.user_id = user_account.id
            user_message.save()

            user_status.user_account = user_account
            user_status.user_id = user_account.id
            user_status.save()

            user_money.user_account = user_account
            user_money.user_id = user_account.id
            user_money.email = user_account.email
            user_money.save()
            return HttpResponsePermanentRedirect(reverse('USER:login'))
        else:
            return render(request, 'user_register.html', {'error':'请检查输入，刷新界面后再尝试！！！'})

# 登录逻辑的实现
class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, "user_login.html", {'login_form': login_form, 'error': ''})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            print(username,pass_word)
            try:
                user_account = UserAccount.objects.get(Q(email=username) & Q(user_pwd=pass_word))
                if user_account:
                    user_message = UserMessage.objects.get(user_id=user_account.id)
                    request.session['user_message'] = model_to_dict(user_message)
                    request.session.set_expiry(60*30)
                    print('a')
                    return HttpResponsePermanentRedirect(reverse('WEB:to_index'))
                else:
                    return render(request, 'user_login.html', {'error': '无此用户，走去注册吗？'})
            except Exception as e:
                return render(request, 'user_login.html', {'error': '帐号或密码错误！！！'})
        else:
            return render(request, 'user_login.html', {'error':'请检查输入！！！'})

# 登出逻辑的实现
class LogoutView(View):

    def get(self, request):
        try:
            del request.session['user_message']
            return HttpResponsePermanentRedirect(reverse('WEB:to_index'))
        except Exception as e:
            return HttpResponsePermanentRedirect(reverse('WEB:to_index'))

# 忘记密码逻辑的实现
class ForgetPwdView(View):

    def get(self, request):
        return render(request, 'index.html')

# 用户中心逻辑的实现
class CenterView(View):

    def get(self, request):
        return render(request, 'user_center.html')

# ajax获取用户资金信息
class MoneyView(View):
    def get(self, request):
        data = {'error':'服务器错误！'}
        user_id = request.GET.get('user_id',None)
        print('user_id = ',user_id)
        try:
            data = UserMoneyCount.objects.get(user_id=user_id)
            return JsonResponse(model_to_dict(data))
        except Exception as e:
            print(e)
            return JsonResponse(data, safe=False)

    def post(self,request):
        print('request_POST',request.POST)
        data = {'error':'服务器错误！'}
        try:
            return JsonResponse(data)
        except Exception as e:
            print(e)
            return JsonResponse(data)