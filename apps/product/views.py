from django.shortcuts import render
from django.views.generic.base import View
from apps.product.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse,HttpResponsePermanentRedirect
from apps.utils import *
from apps.web.models import CacheData
from apps.operation.models import *
from django.forms.models import model_to_dict
from django.urls import reverse
from apps.web_config import CACHE_CART_KEY,CACHE_CART_TIME

# Create your views here.

# 分类页面
class CategoryView(View):
    def get(self, request, category_id):
        print('category_id', category_id)

# 商品页面
class ItemView(View):
    def get(self, request, item_id):
        item = Product.objects.get(id=int(item_id))
        all_review = item.get_review()
        is_cart = False
        # 对评论进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger as p:
            print(p)
            page = 1
        except EmptyPage as e:
            print(e)
            page = 1
        p = Paginator(all_review, 1)
        reviews = p.page(page)
        # 判断此商品是否添加了购物车
        try:
            user_message = request.session['user_message']
            user_id = user_message['user_id']
            list_data = get_data_from_redis(CACHE_CART_KEY, user_id)
            if str(item_id) in list_data:
                is_cart = True
        except Exception as e:
            print(e)
        return render(request, "product_item.html", {
            "item": item,
            "all_review": reviews,
            "is_cart":is_cart,
        })

# 搜索结果页面
class QueryResultView(View):
    def post(self, request):
        pass


# 加入购物车
class AddCartView(View):
    def get(self, request):
        try:
            user_id = request.GET.get('user_id', None)
            product_id = request.GET.get('pid', None)
            del_pid_in_redis(CACHE_CART_KEY, CACHE_CART_TIME, user_id, product_id)# utils
            is_ok = append_pid_to_redis(CACHE_CART_KEY, CACHE_CART_TIME, user_id, product_id)# utils
            if is_ok:
                print('user_id=%s的商品已加入购物车！！！'%user_id)
            else:
                raise Exception('购物车添加失败！！！')
            return HttpResponse("success", content_type='text')
        except Exception as e:
            print(e)
            return HttpResponse('error',content_type='text')

# 购物车页面
class ShoppingCatView(View):
    def get(self, request, item):
        try:
            user_message = request.session['user_message']
            user_id = user_message['user_id']
            list_data = get_data_from_redis(CACHE_CART_KEY, user_id)# utils
            ps,all_product,product_count = [],[],0
            for i in list_data:
                ps.append(Product.objects.filter(id=int(i)))
            for p in reversed(ps):
                all_product.append(p)
                product_count += 1
            return render(request, "user_shoppingCart.html", {
                "all_product": all_product,
                "product_count": product_count,
            })
        except Exception as e:
            print('ShoppingCatView = ', e)
            return HttpResponsePermanentRedirect(reverse('WEB:to_index'))