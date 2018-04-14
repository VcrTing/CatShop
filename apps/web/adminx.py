import xadmin
from .models import *
from xadmin import views
from apps.web_config import *

# 这是设置样式折叠，需把它写在类里面
menu_style = "accordion"

# 设置models的全局图标，图标来源：http://v3.bootcss.com/components/
                    # 图标来源2：http://www.yeahzan.com/fa/facss.html
global_models_icon = {
    WebMessage: "glyphicon glyphicon-user",
}


class WebMessageAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'site_running_time', 'site_front_status', 'register_num', 'oline_num'
    ]


xadmin.site.register(WebMessage, WebMessageAdmin)