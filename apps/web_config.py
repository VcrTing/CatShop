import os,datetime,time

# 地址配置
IMG_BASE_DIR = 'web_site'

# 站点配置
WEB_SITE_TITLE = '猫之商城后台系统'
WEB_SITE_FOOTER = '猫之有限公司'

# 未填写信息的默认值
STR_DEFAULT = '这个人很懒，什么也没留下。'
STR_NUM_DEFAULT = '未填写。'

# 布尔/空布尔默认值
BOOL_DEFAULT = False
BOOL_NULL_DEFAULT = None

# 时间默认值
DATE_DEFAULT = time.asctime( time.localtime(time.time()) )
DATE_TIME_DEFAULT = datetime.datetime.now()

# 金额/积分默认值
INT_DEFAULT = 0
DECIMAL_DEFAULT_ZERO = 0.0

# 图片默认值
FACE_DEFAULT = os.path.join(IMG_BASE_DIR, 'default_face.png')

NOTFOUND_IMG_DEFAULT = os.path.join(IMG_BASE_DIR, 'notfound.png')

# 状态默认值
STATUS_STR_DEFAULT = '1'

# 购物车缓存键
CACHE_CART_KEY = 'catshop_cart_user_id='
# 购物车存活时间
CACHE_CART_TIME = 60*60*24*3

# 订单数据中转键
CACHE_ORDER_KEY = 'catshop_order_user_id='
CACHE_ORDER_TIME = 60*30
