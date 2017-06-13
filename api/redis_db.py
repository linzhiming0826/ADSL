# encoding:utf-8
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class RedisDB:
    @classmethod
    def proxy(self):
        '''
        获取redis链接
        '''
        pool = redis.ConnectionPool(
            host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)
        return redis.Redis(connection_pool=pool)


if __name__ == '__main__':
    print RedisDB.proxy()
