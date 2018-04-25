
from django.conf import settings
from django.core.cache import cache
import json,redis
from apps.web_config import *

#----------------------------------------tag----------------------------------------

def read_dict_from_cache( data_key_list=[]):
    '''
    读取缓存数据库
    :param data_key_list: 装有key的数组
    :return: data_list是数组，里面每一个元素都是一个字典，字典里面是key与value
    '''
    data_list = []
    for i in data_key_list:
        value = cache.get(i)
        if value:
            data_list.append(json.loads(value))
    return data_list

def write_dict_to_cache( data_dict):
    '''
    写入缓存数据库
    :param data_dict: 数据字典，里面有key与value
    :return: Boolean
    '''
    try:
        for i,v in enumerate(data_dict):
            cache.set(i, json.dumps(v), settings.NEVER_REDIS_TIMEOUT)
        return True
    except Exception as e:
        print(e)
        return False

#----------------------------------------tag----------------------------------------

# 购物车缓存键
# CACHE_KEY = 'catshop_user_id='

# redis连接池
pool = redis.ConnectionPool(host='localhost', port=6379)

# 往redis中追加商品id
def append_pid_to_redis(CACHE_KEY, CACHE_TIME, user_id, item_id):
    try:
        r = redis.Redis(connection_pool=pool)
        old_data = get_data_from_redis(CACHE_KEY, user_id)
        if item_id not in old_data:
            r.append(CACHE_KEY+str(user_id),','+str(item_id))
            r.expire(CACHE_KEY+str(user_id), CACHE_TIME)
            return True
        return False
    except Exception as e:
        return False

# 覆盖redis中user_id为键的数据
def set_list_to_redis(CACHE_KEY, CACHE_TIME, user_id, item_list = []):
    try:
        save_str = ''
        r = redis.Redis(connection_pool=pool)
        if item_list:
            for pid in item_list:
                save_str = save_str+','+str(pid)
        r.set(CACHE_KEY+str(user_id), save_str)
        r.expire(CACHE_KEY+str(user_id), CACHE_TIME)
        return True
    except Exception as e:
        return False

# 获取redis中的数据，返回list
def get_data_from_redis(CACHE_KEY, user_id):
    try:
        r = redis.Redis(connection_pool=pool)
        str_cache_data = r.get(CACHE_KEY + str(user_id))
        if str_cache_data:
            str_cache_data = str_cache_data.decode()
            list_cache_data = str_cache_data.split(',')
            list_cache_data.remove(list_cache_data[0])
            return list_cache_data
        else:
            return []
    except Exception as e:
        raise e

# 删除redis中的一个id数据
def del_pid_in_redis(CACHE_KEY, CACHE_TIME, user_id, item_id):
    try:
        r = redis.Redis(connection_pool=pool)
        old_data = get_data_from_redis(CACHE_KEY, user_id)
        new_data = [old_item_id for old_item_id in old_data if item_id != old_item_id]
        set_list_to_redis(CACHE_KEY, CACHE_TIME, user_id, new_data)
        return True
    except Exception as e:
        return False