# encoding:utf-8
import re
import commands
import requests
import time
import hashlib
from config import *


class Main(object):
    @classmethod
    def _get_ip(self):
        '''
        获取ip
        '''
        status, output = commands.getstatusoutput('ifconfig')
        if status == 0:
            result = re.search(
                '1492\s+?inet\s+?(\d+\.\d+\.\d+\.\d+)\s+?netmask', output)
            if result:
                return result.group(1)

    @classmethod
    def _send_ip(self, ip):
        '''
        发送新的ip到服务端
        '''
        try:
            value = '%s:%s' % (ip, ASDL_PORT)
            token = hashlib.md5('%s%s%s' % (CODE, value, SECRET)).hexdigest()
            data = {'key': CODE, 'value': value, 'token': token}
            text = requests.post(SERVER_URL, data).text
            print text
        except Exception as e:
            print e

    @classmethod
    def restart_adsl(self):
        '''
        进行重新拨号
        1.首先进行adsl的拨号
        2.进行拨号后ip的获取
        3.将新的ip发送到服务端
        4.等待一段时间，继续程序以及出现错误的一些处理方式
        '''
        while 1:
            print 'adsl will restart'
            status, output = commands.getstatusoutput(ADSL_BASH)
            if status == 0:
                print 'adsl start successfully'
                ip = self._get_ip()
                if ip:
                    print 'new ip: %s' % ip
                    self._send_ip(ip)
                    print 'wait %s seconds' % ADSL_CYCLE
                    time.sleep(ADSL_CYCLE)
                else:
                    print 'ip is null or empty'
            else:
                print 'adsl start is failed'
            time.sleep(1)


if __name__ == '__main__':
    print Main.restart_adsl()
