# encoding:utf-8
import random
from config import REDIS_PROXY_KEY
from redis_db import RedisDB


class Proxy(object):
    @classmethod
    def get_proxy(self, module):
        '''
        获取代理，暂时只实现获取某一台代理的方法，可以自己扩展，随机获取
        '''
        result = {'rt': '0', 'msg': 'not proxy', 'proxy': None}
        if module == 'one':
            keys = RedisDB.proxy().hkeys(REDIS_PROXY_KEY)
            key = random.choice(keys)
            proxy = RedisDB.proxy().hget(REDIS_PROXY_KEY, key)
            if proxy:
                result = {'rt': '1', 'msg': 'success', 'proxy': proxy}
        return result

    @classmethod
    def add_proxy(self, **kwargs):
        '''
        设置代理
        '''
        RedisDB.proxy().hset(REDIS_PROXY_KEY, kwargs['key'], kwargs['value'])
        return {'rt': '1', 'msg': 'success'}
