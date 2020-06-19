import requests
import params
import json

class GD:
    def __init__(self):
        self.key = params.key

    def getGaodeLocation(self, lat, lng):
        url = "https://restapi.amap.com/v3/assistant/coordinate/convert"

        params = {
            'key': self.key,
            'locations': lng + ',' + lat,
            'coordsys': 'baidu',
            'output': 'JSON'
        }

        res = requests.get(url, params=params)

        return res


# 转换高德经纬度
def getGaodeLocation(lat, lng):
    res = GD().getGaodeLocation(lat, lng)

    res = json.loads(res.text)

    return res['locations']
