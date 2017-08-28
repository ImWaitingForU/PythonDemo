# coding=utf-8
import urllib
import urllib2

# proxy设置
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http", "代理服务器地址"})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

# post请求 通过Request方法传递data
values = {"keyword": "iwfu"}
data = urllib.urlencode(values)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
request = urllib2.Request("http://www.baiduaaaa.com", data)
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
    print e.reason

# get请求 直接拼接在req后面
# values = {}
# values['username'] = "1016903103"
# values['password'] = "XXXX"
# data = urllib.urlencode(values)
# url = "http://www.baidu.com"
# getUrl = url + "?"+values
# req = urllib2.Request(getUrl)
# res = urllib.urlopen(req)
# print res.read()
