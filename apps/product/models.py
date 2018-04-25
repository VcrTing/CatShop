from django.db import models
from apps.web_config import *
from apps.user.models import UserAccount
# Create your models here.

# 分类
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"分类名")
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"产品大分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 产品表
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"产品名称", default=STR_NUM_DEFAULT)
    sub_title = models.CharField(max_length=250, verbose_name=u"小标题", default=STR_NUM_DEFAULT)
    orignal_price = models.FloatField(verbose_name=u"原始价格", default=DECIMAL_DEFAULT_ZERO)
    promote_price = models.FloatField(verbose_name=u"优惠价格", default=DECIMAL_DEFAULT_ZERO)
    stock = models.CharField(max_length=30, verbose_name=u"库存", default='0')
    create_time = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)
    sale_count = models.IntegerField(verbose_name=u"销售数量", default=0)
    status = models.NullBooleanField(verbose_name=u'销售状态', default=STR_NUM_DEFAULT)
    category = models.ForeignKey(Category, verbose_name=u"分类", on_delete=models.SET_NULL, blank=True, null=True)
    business_name = models.CharField(max_length=250, verbose_name=u'商家名称')

    # 后台菜单、title等显示名称
    class Meta:
        verbose_name = u"产品表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_title_image(self):
        try:
            num = self.productsingleimage_set.all()[0]
            return num
        except Exception as e:
            print(e)
            return None

    def get_single_image(self):
        return self.productsingleimage_set.all()

    def get_detail_image(self):
        return self.productdetailimage_set.all()

    def get_property_value(self):
        return self.propertyvalue_set.all()

    def get_review(self):
        return self.review_set.all()

    def get_subtitle(self):
        return self.sub_title.split(" ")[0]

# 属性
class Property(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"属性")
    category = models.ForeignKey(Category, verbose_name=u"分类", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = u"产品属性"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 属性值
class PropertyValue(models.Model):
    value = models.CharField(max_length=200, verbose_name=u"属性值")
    property = models.ForeignKey(Property, verbose_name=u"属性名", on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name=u"所属商品", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = u"属性值"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value

# 产品图片标题图
class ProductSingleImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=u"所属商品", on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to=os.path.join('produceImage','Single'), default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"产品标题图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

# 产品图片详情图
class ProductDetailImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=u"所属商品", on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to=os.path.join('produceImage','Detail'), default=NOTFOUND_IMG_DEFAULT, max_length=100)

    class Meta:
        verbose_name = u"产品详情图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)

# 产品评价
class Review(models.Model):
    content = models.TextField(verbose_name=u"评价内容")
    product = models.ForeignKey(Product, verbose_name=u"所属商品", on_delete=models.SET_NULL, blank=True, null=True)
    user_account = models.ForeignKey(UserAccount, verbose_name=u"所属用户", on_delete=models.SET_NULL, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)
    ratings = models.IntegerField(verbose_name=u'评价星', default=INT_DEFAULT)

    class Meta:
        verbose_name = u"产品评价"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
