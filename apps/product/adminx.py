import xadmin
from .models import *
from apps.web_config import *

site_title = WEB_SITE_TITLE
site_footer = WEB_SITE_FOOTER

class CategoryAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'name', 'create_time'
    ]

class ProductAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'name', 'orignal_price', 'promote_price', 'stock', 'sale_count', 'status', 'create_time'
    ]

class PropertyAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'name', 'category'
    ]

class PropertyValueAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'value', 'property', 'product'
    ]

class ProductSingleImageAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'product', 'image'
    ]

class ProductDetailImageAdmin(object):

    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'product', 'image'
    ]

class ReviewAdmin(object):
    site_title = WEB_SITE_TITLE
    site_footer = WEB_SITE_FOOTER

    list_display = [
        'content', 'product', 'ratings', 'create_time'
    ]

xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Property, PropertyAdmin)
xadmin.site.register(PropertyValue, PropertyValueAdmin)
xadmin.site.register(ProductSingleImage, ProductSingleImageAdmin)
xadmin.site.register(ProductDetailImage, ProductDetailImageAdmin)
xadmin.site.register(Review, ReviewAdmin)
