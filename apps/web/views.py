from django.shortcuts import render

# Create your views here.
def to_index(request):
    '''
    转发到网站的主界面，Index界面
    :param request:
    :return:render
    '''
    return render(request,'index.html')

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