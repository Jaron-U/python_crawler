import urllib.request
import urllib.parse
import json
import time
while 1:
    content = input("Please input the content you want to translate(press # to exit):")
    # if (content == "#"):
    #     break

    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode()

    response = urllib.request.urlopen(url, data)

    html = response.read().decode()
    html = json.loads(html)

    result = html["translateResult"][0][0]["tgt"]
    print("Result:",result)

#     # # 隐藏爬虫
#     # time.sleep(5)


# ###使用代理地址
# import urllib.request
# import random

# url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# iplist = ['106.40.145.198:8080', '113.120.60.90:8080', '223.243.69.218:8888']

# proxy_support = urllib.request.ProxyHandler({'http':'113.120.60.90:8080'})
# # proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
# opener = urllib.request.build_opener(proxy_support)
# opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15')]

# urllib.request.install_opener(opener)

# response = urllib.request.urlopen(url)
# html = response.read().decode('utf-8')

# print(html)


