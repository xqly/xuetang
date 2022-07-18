import requests
import json 
import time
url = "https://api.sisensing.com/follow/app/list?pageNum=1&pageSize=3&status=3"

headers ={
    "Authorization":"150b8e44-de0e-4865-98e5-71fbeecd3e81",
    "content-type":"application/json",
    "Connection":"keep-alive",
    "user_type":"USER",
    "Accept-Encoding":"gzip,compress,br,deflate",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.25(0x18001925) NetType/4G Language/zh_CN",
    "Referer":"https://servicewechat.com/wx49bc05db1e528fe4/25/page-frame.html"
}

while True:
    res = requests.get(url,headers= headers)

    dd = json.loads(res.text)
    num = dd['data']['records'][0]['followedDeviceGlucoseDataPO']['latestGlucoseValue']
    num = float(num)
    print(num)
    if num>5.1:
        print((num-5.1)*0.35)
    time.sleep(100)
    