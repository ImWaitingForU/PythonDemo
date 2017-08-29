# coding=utf-8

"""
    爬虫练习:爬取糗事百科段子
    Rose
    2017-8-29 22:31:50
"""

import urllib
import urllib2
import re

qiushibaike_url = 'http://www.qiushibaike.com/'


def main():
    url = qiushibaike_url + 'hot/page/' + '2'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Referer': url}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        # print content
        # 待修改正则表达式
        pattern = re.compile('h2>(.*?)</h2.*?content">(.*?)</.*?number">(.*?)</',re.S)

        items = re.findall(pattern, content)
        print 'result长度：' + str(len(items))
        for item in items:
            # 过滤掉有图片的
            # haveImg = re.search("img", item[2])
            # if not haveImg:
                print item[0], item[1], item[2]

    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason


if __name__ == '__main__':
    main()
