from django.shortcuts import render
from django.views.generic.base import View
from apps.product.models import Product,Category
#from apps.operation.models import OrderItem
#from apps.user.models import UserAccount

# Create your views here.
# 首页
class IndexView(View):

    def get(self, request):
        all_category = Category.objects.all()

        all_product = Product.objects.all()
        '''user_message = request.session['user_message']
        print('session.user_message = ', user_message)
        if user_message:
            user_account = user_message.user_id
            print('user_account', user_account)'''
        #还需要查询购物车
        return render(request, "index.html", {
            "all_category": all_category,
            "all_product": all_product,
            #"user": user_account,
            #"user_product_cat": user_cat_count
        })

    def post(self, request):
        print('index_post')


#----------------------------------------tag----------------------------------------
def error_400(request):
    '''
    400错误界面
    :param request:
    :return:
    '''
    print('400')
    return render(request, 'error_page.html',{'error_code':'400'})

def error_403(request):
    '''
    403错误界面
    :param request:
    :return:
    '''
    print('403')
    return render(request, 'error_page.html',{'error_code':'403'})

def error_404(request):
    '''
    404错误界面
    :param request:
    :return:
    '''
    print('404')
    return render(request, 'error_page.html',{'error_code':'404'})

def error_500(request):
    '''
    500错误界面
    :param request:
    :return:
    '''
    print('500')
    return render(request, 'error_page.html',{'error_code':'500'})