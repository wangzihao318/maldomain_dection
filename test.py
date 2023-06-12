# encoding:utf-8

"""
使用内部DNS服务器获取域名的ns服务器和其ttl时间
作者：程亚楠
时间：2017.10.18
注意事项：
因为部分域名的zone文件配置错误，导致无法获取ns服务器，但是其可正常解析，例如dxi5.com

todo:
ddddd

"""

import DNS
import tldextract


print(DNS.dnslookup('www.baidu.com', qtype='A') )




