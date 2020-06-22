import requests
import time
import sys
import time
import hashlib
import base64
# 流量订单使用
_version = sys.version_info
is_python3 = (_version[0] == 3)
orderId = "O20062014011915934858"
secret = "d8e5571418e1ace90b05fa264f44f10e"
host = "flow.hailiangip.com"
port = "14223"
user = "proxy"
timestamp = str(int(time.time()))                # 计算时间戳
txt = "orderId=" + orderId + "&" + "secret=" + secret + "&" + "time=" + timestamp
if is_python3:
    txt = txt.encode()
sign = hashlib.md5(txt).hexdigest()                 # 计算sign
password = 'orderId='+orderId+'&time='+timestamp+'&sign='+sign+"&pid=-1"+"&cid=-1"+"&uid="+"&sip=0"+"&nd=1"
targetUrl = "http://api.hailiangip.com:8422/api/myIp"


def generate():
    proxyUrl = "http://" + user + ":" + password + "@" + host + ":" + port
    proxy = {"http": proxyUrl, "https": proxyUrl}

    return proxy


if __name__ == '__main__':
    generate()
