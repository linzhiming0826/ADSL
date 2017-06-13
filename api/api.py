# encoding:utf-8
from flask import Flask, jsonify, request, abort
from proxy import Proxy
from decorators import Decorators

api = Flask(__name__)


@api.route('/api/v1/proxy', methods=['POST'])
@Decorators.proxy_auth
@Decorators.jsonp
def add_proxy():
    '''
    新增一个代理
    '''
    dic = request.form.to_dict()
    return jsonify(Proxy.add_proxy(**dic))


@api.route('/api/v1/proxy', methods=['GET'])
@Decorators.jsonp
def get_proxy():
    '''
    获取一个代理
    '''
    module = request.args.get('module', False)
    return jsonify(Proxy.get_proxy(module)) if module else abort(404)


if __name__ == '__main__':
    api.run(debug=False, host='0.0.0.0', port='5000')
