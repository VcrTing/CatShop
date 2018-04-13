from django.shortcuts import render

# Create your views here.
def to_index(request):
    '''
    跳转至用户个人中心界面
    :param request:
    :return: user_index.html
    '''
    return render(request,'user_index.html')