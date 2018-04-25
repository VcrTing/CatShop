from django.shortcuts import render,redirect,render_to_response
from django.views.generic.base import View
from django.http import HttpResponsePermanentRedirect,HttpResponseRedirect
from apps.product.models import *
from apps.user.models import *
from apps.operation.models import *
from django.urls import reverse
from django.db.models import Q
import random,time,decimal
from apps.utils import *
from django.utils.timezone import now
from apps.web_config import CACHE_CART_KEY,CACHE_CART_TIME,CACHE_ORDER_KEY,CACHE_ORDER_TIME

# Create your views here.

# 重定向到支付界面
class GoPayView(View):
    def get(self, request):
        user_id = request.session['user_id']
        product_id = request.session['product_id']
        order = request.session['order']

        all_oi = OrderItem.objects.filter(order_id__isnull=True, user_account_id=user_id, product_id=product_id)
        all_unit = 0
        for oi in all_oi:
            oi.order = order
            oi.save()
            unit = oi.product.promote_price * oi.number
            all_unit += unit
        return render(request, 'order_payment.html', {
            "all_unit": all_unit,
            "order_item": all_oi,
        })

    def post(self, request):
        print('GoPayView.POST!!!')
        return HttpResponseRedirect(reverse('WEB:to_index'))

# 结算页面
class BuyView(View):
    def get(self, request):
        print('BuyView.GET')
        all_unit = request.GET.get("all_unit", None)
        order = request.GET.get("order", None)
        return render(request, "order_settlement.html", {
                "all_unit": all_unit,
                "order": order,
        })

    def post(self, request):
        try:
            user_message = request.session['user_message']
            user_id = user_message['user_id']
            user_account = UserAccount.objects.get(id=user_id)
            product_id = request.POST.get('product_id', None)
            order = Order()
            order.address = request.POST.get('address','未确认地址！')
            if not order.address:
                raise Exception('没填写信息！！！')
            order.post = request.POST.get('post',000000)
            order.receiver = request.POST.get('receiver', user_id)
            order.mobile = request.POST.get('mobile', user_account.phone)
            order.user_msg = request.POST.get('user_msg', '无备注。')
            order.order_code = int(datetime.datetime.now().strftime('%y%m%d%H%M%S')) * 10000 + random.randint(0, 9999)
            order.status = "waitPay"
            order.user = user_account
            order.save()

            try:
                order_item_id = request.POST.get('oiid')
                order_item = OrderItem(id=order_item_id)
                order_item.order_code = order.order_code
                order_item.number = request.POST.get('number')
                order_item.product = Product.objects.get(id=product_id)
                order_item.user_account = UserAccount.objects.get(id=user_id)
                order_item.save()
            except Exception as e:
                print(e)

            request.session['order'] = order
            request.session['user_id'] = user_id
            request.session['product_id'] = product_id
            return HttpResponseRedirect(reverse('OPERATION:go_pay'))
        except Exception as e:
            print('BuyView.Excaption = ',e)
            return HttpResponsePermanentRedirect(reverse('WEB:to_index'))

# 立即购买
class BuyOneView(View):
    def get(self, request):
        item_id = request.GET.get('pid', None)
        num = int(request.GET.get('num', None))
        product_item = Product.objects.get(id=int(item_id))
        user_message = request.session['user_message']
        user_id = user_message['user_id']
        user_account = UserAccount.objects.get(id=user_id)

        all_oi = OrderItem.objects.filter(Q(user_account_id=user_id)& Q(order_id__isnull=True))
        found = False
        for oi in all_oi:
            if oi.product.id == product_item.id:
                oi.number = num
                oi.save()
                found = True
        if not found:
            oi = OrderItem()
            oi.number = num
            oi.product_id = item_id
            oi.user_id = user_id
            oi.user_account = user_account
            oi.save()
        all_oi_list = OrderItem.objects.filter(Q(user_account_id=user_id)& Q(order_id__isnull=True))
        all_oi_id = []
        for all_oi in all_oi_list:
            all_oi_id.append(all_oi.id)

        all_oi,total = [],0
        for oiid in all_oi_id:
            oi = OrderItem.objects.get(id=int(oiid))
            all_oi.append(oi)
            total += oi.product.promote_price * oi.number
        return render(request, "order_settlement.html", {
            "all_order_item": all_oi,
            "all_unit": total,
        })

# 点击确认支付，跳转到支付成功页面
class PayedView(View):
    def get(self, request):
        user_id = request.GET.get('user_id')
        order_item_id = request.GET.get('oid')

        print('支付成功！！！')
        return render(request, 'index.html')

    def post(self, request):
        try:
            old_time = time.time()
            print('PayedView.POST!!!')
            # 获取订单数据
            user_id = request.POST.get('user_id')
            order_item_id = request.POST.get('oid')
            if OrderItem.objects.filter(id=order_item_id)[0]:
                order_item = OrderItem.objects.filter(id=order_item_id)[0]
                # 改变订单状态为待收货
                order = Order.objects.get(order_code=order_item.order_code)
                order.status = 'waitDelivery'
                order.delivery_time = now()
                order.save()
                product_id = order.product_id

                # 改变商品销售数量，+1
                product = order_item.product
                product.sale_count += 1
                product.save()

                try:
                    # 删除购物车商品
                    del_pid_in_redis(CACHE_CART_KEY, CACHE_CART_TIME, user_id, product_id)

                    # 增加用户消费记录
                    user_money = UserMoneyCount.objects.get(user_account_id=user_id)
                    user_money.use_money_count += decimal.Decimal(product.promote_price)
                    user_money.product_num += order_item.number
                    user_money.save()
                except Exception as e:
                    print(e)

            print('sys_use_time = ', time.time()-old_time)
            return HttpResponsePermanentRedirect(reverse('OPERATION:user_order'))
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse('WEB:to_index'))

# 我的订单页
class MyOrderView(View):
    def get(self, request):
        try:
            user_message = request.session['user_message']
            print('MyOrderView.GET!!!')
            order = Order.objects.filter(orderitem__isnull=False, user_id=user_message['user_id']).exclude(status="delete")
            return render(request, 'order_myOrder.html', {
                'orders':order,
            })
        except Exception as e:
            return HttpResponsePermanentRedirect(reverse('WEB:to_index'))

# 订单界面去付款
class SettlementView(View):
    def get(self, request):
        print('SettlementView.GET')
        return HttpResponsePermanentRedirect(reverse('WEB:to_index'))

    def post(self, request):
        try:
            order_item_id = request.POST.get('oid')
            user_id = request.POST.get('user_id')
            all_oi = OrderItem.objects.filter(user_account_id=user_id, id=order_item_id, order__isnull=False)
            all_unit = 0
            for oi in all_oi:
                unit = oi.product.promote_price * oi.number
                all_unit += unit
            return render(request, 'order_payment.html', {
                "all_unit": all_unit,
                "order_item": all_oi,
            })
        except Exception as e:
            print('SettlementView.Exception = ', e)
            return HttpResponsePermanentRedirect(reverse('WEB:to_index'))

# 催卖家发货->已收货物
class GetGoodsView(View):

    def post(self, request):
        try:
            order_code = request.POST.get('order_code')

            # 更改订单项状态
            order_item = OrderItem.objects.get(order_code=order_code)
            order_item.status = 'confirm'
            order_item.save()

            # 更改订单状态
            order = order_item.order
            order.confirm_time = now()
            order.status = 'waitConfirm'
            order.save()

            print('GetGoodsView.POST!!!')
            return HttpResponsePermanentRedirect(reverse('OPERATION:user_order'))
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse('WEB:to_index'))

# 已收货物->待评价
class GotGoodsView(View):

    def post(self, request):
        try:
            order_code = request.POST.get('order_code')

            # 更改订单项状态
            order_item = OrderItem.objects.get(order_code=order_code)
            order_item.status = 'finish'
            order_item.save()

            # 更改订单状态
            order = order_item.order
            order.confirm_time = now()
            order.status = 'finish'
            order.save()

            print('GetGoodsView.POST!!!')
            return HttpResponsePermanentRedirect(reverse('OPERATION:user_order'))
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse('WEB:to_index'))