import urllib2

proxies = {"http": "61.140.104.98:6666"}
proxy_s = urllib2.ProxyHandler(proxies)
opener = urllib2.build_opener(proxy_s)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://wwww.baidu.com').read()
print content
