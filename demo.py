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
# values = {"keyword": "iwfu"}
# data = urllib.urlencode(values)
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
# request = urllib2.Request("http://www.baiduaaaa.com", data)
# try:
#     response = urllib2.urlopen(request)
# except urllib2.HTTPError, e:
#     print e.code
#     print e.reason

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

# 获取Cookie,并打印信息
import cookielib

#
# cookie = cookielib.CookieJar()
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# res = opener.open("http://www.baidu.com")
# for item in cookie:
#     print 'name = ' + item.name
#     print 'value = ' + item.value
# # 保存cookie
# cookie = cookielib.MozillaCookieJar("roseCookie.txt")
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# res2 = opener.open("https://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件获取cookie读取
# cookie = cookielib.MozillaCookieJar()
# cookie.load("roseCookie.txt", ignore_expires=True, ignore_discard=True)
# req = urllib2.Request("http://www.baidu.com")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

# 测试登录CSDN并获取cookie保存到本地
# fileName = "JuejinCookie.txt"
# cookie = cookielib.MozillaCookieJar(fileName)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postData = urllib.urlencode({'loginPhoneOrEmail': '870536460@qq.com', 'loginPassword': 'fengacheng1996'})
# loginUrl = 'https://juejin.im/'
#
# result = opener.open(loginUrl, postData)
# # 保存该cookie
# cookie.save(ignore_expires=True, ignore_discard=True)
# # 使用改cookie访问后面的网站，，，，爬取后面的数据
# grantUrl = 'https://juejin.im/user/5739c8f92e958a0066f5ee4c'
# result = opener.open(grantUrl)
# print result.read()

# 正则表达式
import re
# 设置正则表达式规则
pattern = re.compile(r'rosechan')
# 调用match进行匹配
testString = 'rosechanchanrosechan'
result1 = re.match(pattern, testString)
result2 = re.search(pattern, testString)

print result1.group()
print result2.group()
