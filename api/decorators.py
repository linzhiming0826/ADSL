# encoding:utf-8
import hashlib
from functools import wraps
from flask import request, current_app, abort


class Decorators:
    @classmethod
    def jsonp(self, func):
        '''
        修饰器：将结果转化成jsonp输出
        '''

        @wraps(func)
        def wrapper(*args, **kwargs):
            callback = request.args.get('callback', False)
            if callback:
                content = str(callback) + '(' + str(
                    func(*args, **kwargs).data) + ')'
                return current_app.response_class(
                    content, mimetype='application/javascript')
            else:
                return func(*args, **kwargs)

        return wrapper

    @classmethod
    def proxy_auth(self, func):
        '''
        修饰器：验证新增代理参数是否正确
        '''

        @wraps(func)
        def wrapper(*args, **kwargs):
            dic = request.form.to_dict()
            if dic['token'] and dic['key'] and dic['value']:
                token_local = hashlib.md5(
                    '%s%sproxy' % (dic['key'], dic['value'])).hexdigest()
                if dic['token'] == token_local:
                    return func(*args, **kwargs)
            return abort(404)

        return wrapper
