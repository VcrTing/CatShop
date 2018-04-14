"""reWrite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler400,handler403,handler404,handler500
import xadmin
from xadmin.plugins import xversion
xadmin.autodiscover()
xversion.register_models()

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('',include('web.urls', namespace='WEB')),
    path('user/',include('user.urls', namespace='USER')),
    path('operation/',include('operation.urls', namespace='OPERATION')),
    path('product/',include('product.urls', namespace='PRODUCT')),
]

# ERROR PAGE（错误界面）
handler400 = 'web.views.error_400'
handler403 = 'web.views.error_403'
handler404 = 'web.views.error_404'
handler500 = 'web.views.error_500'