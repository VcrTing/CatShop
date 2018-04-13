from django.shortcuts import render

# Create your views here.
def to_index(request):
    '''
    转发到网站的主界面，Index界面
    :param request:
    :return:render
    '''
    return render(request,'web_index.html')