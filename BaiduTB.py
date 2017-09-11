# coding=utf-8
"""
爬取百度贴吧
2017年8月31日21:51:52
"""

import urllib2
import re
import urllib


# 百度贴吧爬虫类
class BDTB:
    """
    初始化参数
    @:param baseUrl : 基础url
    @:param seeLZ : 页面参数，表示是否只查看楼主
    """

    def __init__(self, base_url, see_lz):
        self.baseURL = base_url
        self.seeLZ = '?see_lz=' + str(see_lz)

    # 传入页码，获取该帖子的代码
    def get_page(self, page_num):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(page_num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"链接百度贴吧失败", e.reason
                return None

    # 获取帖子标题
    def get_title(self):
        page = self.get_page(1)
        reg = '<h3 class="core_title_txt.*?>(.*?)</h3>'
        pattern = re.compile(reg, re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            # print result.group(1).strip()
        else:
            return None


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
# bdtb.get_page(1)
bdtb.get_title()
