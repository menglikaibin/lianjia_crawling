import requests
import time
import tqdm
import json
import sqlite3
import numpy
import math
import hashlib
import params
import pymysql
import DB
import random

sql_InsertDetailInfo = '''insert into %s(houseId,houseCode,title,appid,source,imgSrc,layoutImgSrc,imgSrcUri,layoutImgSrcUri,roomNum,square,buildingArea,buildYear,isNew,ctime,mtime,orientation,floorStat,totalFloor,decorateType,hbtName,isYezhuComment,isGarage,houseType,isFocus,status,isValid,signTime,signSource,signSourceCn,isDisplay,address,community,communityId,communityName,communityUrl,communityUrlEsf,districtId,districtUrl,districtName,regionId,regionUrl,regionName,bbdName,bbdUrl,houseCityId,subwayInfo,schoolName,schoolArr,bizcircleFullSpell,house_video_info,price,unitPrice,viewUrl,listPrice,publishTime,isVilla,villaNoFloorLevel,villaName,tags)values(:houseId,:houseCode,:title,:appid,:source,:imgSrc,:layoutImgSrc,:imgSrcUri,:layoutImgSrcUri,:roomNum,:square,:buildingArea,:buildYear,:isNew,:ctime,:mtime,:orientation,:floorStat,:totalFloor,:decorateType,:hbtName,:isYezhuComment,:isGarage,:houseType,:isFocus,:status,:isValid,:signTime,:signSource,:signSourceCn,:isDisplay,:address,:community,:communityId,:communityName,:communityUrl,:communityUrlEsf,:districtId,:districtUrl,:districtName,:regionId,:regionUrl,:regionName,:bbdName,:bbdUrl,:houseCityId,:subwayInfo,:schoolName,:schoolArr,:bizcircleFullSpell,:house_video_info,:price,:unitPrice,:viewUrl,:listPrice,:publishTime,:isVilla,:villaNoFloorLevel,:villaName,:tags)'''
sql_CreateDetailInfo = '''create table %s (houseId PRIMARY  KEY 
            , houseCode, title, appid, source, imgSrc, layoutImgSrc, imgSrcUri,
            layoutImgSrcUri, roomNum, square, buildingArea, buildYear, isNew, ctime,
            mtime, orientation, floorStat, totalFloor, decorateType, hbtName,
            isYezhuComment, isGarage, houseType, isFocus, status, isValid, signTime,
            signSource, signSourceCn, isDisplay, address, community, communityId,
            communityName, communityUrl, communityUrlEsf, districtId, districtUrl,
            districtName, regionId, regionUrl, regionName, bbdName, bbdUrl, houseCityId,
            subwayInfo, schoolName, schoolArr, bizcircleFullSpell, house_video_info , price,
            unitPrice, viewUrl, listPrice, publishTime, isVilla, villaNoFloorLevel,
            villaName, tags)'''

class Lianjia():
    def __init__(self, city):
        self.city_dict = params.city_dict
        self.city = city
        self.city_id = self.city_dict[city]['city_id']
        self.url_fang = params.url_fang
        self.url = params.url
        self.cookies = params.cookies
        self.headers = params.headers
        self.proxies = params.proxies

    def GetMD5(self, string_):
        m = hashlib.md5()
        m.update(string_.encode('utf-8'))
        return m.hexdigest()

    def GetAuthorization(self, dict_) -> str:
        datastr = "vfkpbin1ix2rb88gfjebs0f60cbvhedlcity_id={city_id}group_type={group_type}max_lat={max_lat}" \
                  "max_lng={max_lng}min_lat={min_lat}min_lng={min_lng}request_ts={request_ts}".format(
            city_id=dict_["city_id"],
            group_type=dict_["group_type"],
            max_lat=dict_["max_lat"],
            max_lng=dict_["max_lng"],
            min_lat=dict_["min_lat"],
            min_lng=dict_["min_lng"],
            request_ts=dict_["request_ts"])
        authorization = self.GetMD5(datastr)
        return authorization

    def GetDistrictInfo(self) -> list:
        time_13 = int(round(time.time() * 1000))
        authorization = Lianjia(self.city).GetAuthorization(
            {
                'group_type': 'district',
                'city_id': self.city_id,
                'max_lat': self.city_dict[self.city]['max_lat'],
                'min_lat': self.city_dict[self.city]['min_lat'],
                'max_lng': self.city_dict[self.city]['max_lng'],
                'min_lng': self.city_dict[self.city]['min_lng'],
                'request_ts': time_13
            }
        )

        url = self.url % (
            self.city_id, 'district', self.city_dict[self.city]['max_lat'], self.city_dict[self.city]['min_lat'],
            self.city_dict[self.city]['max_lng'], self.city_dict[self.city]['min_lng'], '%7B%7D', time_13,
            authorization, time_13)

        with requests.Session() as sess:
            ret = sess.get(url=url, headers=self.headers, cookies=self.cookies, proxies=self.proxies)

            house_json = json.loads(ret.text[43:-1])

            if house_json['errno'] == 0:

                return house_json['data']['list'].values()

            else:
                return None

    def getBizcircleInfo(self, max_lat, min_lat, max_lng, min_lng):
        time_13 = int(round(time.time() * 1000))
        authorization = Lianjia(self.city).GetAuthorization(
            {
                'group_type': 'bizcircle',
                'city_id': self.city_id,
                'max_lat': max_lat,
                'min_lat': min_lat,
                'max_lng': max_lng,
                'min_lng': min_lng,
                'request_ts': time_13
            })

        url = self.url % (
            self.city_id,
            'bizcircle',
            max_lat,
            min_lat,
            max_lng,
            min_lng,
            '%7B%7D',
            time_13,
            authorization,
            time_13
        )

        with requests.Session() as sess:
            ret = sess.get(url=url, headers=self.headers, cookies=self.cookies)

            house_json = json.loads(ret.text[43:-1])

            if house_json['errno'] == 0:

                return house_json['data']['list'].values()

            else:
                return None

    def GetCommunityInfo(self, max_lat, min_lat, max_lng, min_lng) -> list:
        time_13 = int(round(time.time() * 1000))
        authorization = Lianjia(self.city).GetAuthorization(
            {
                'group_type': 'community',
                'city_id': self.city_id,
                'max_lat': max_lat,
                'min_lat': min_lat,
                'max_lng': max_lng,
                'min_lng': min_lng,
                'request_ts': time_13
            }
        )

        url = self.url % (
            self.city_id, 'community', max_lat, min_lat, max_lng, min_lng, '%7B%7D', time_13, authorization, time_13)

        with requests.Session() as sess:
            ret = sess.get(url=url, headers=self.headers, cookies=self.cookies)
            house_json = json.loads(ret.text[43:-1])

            if house_json['errno'] == 0:
                data_list = []
                if type(house_json['data']['list']) is dict:
                    for x in house_json['data']['list']:
                        data_list.append(house_json['data']['list'][x])
                    return data_list
                else:
                    return house_json['data']['list']

            else:
                return None


## 保存城市区的边界
def saveDistrictBorderIntoDB(city):
    ret = Lianjia(city).GetDistrictInfo()
    cityId = DB.getCityId(city)
    pbar = tqdm.tqdm(ret)

    for x in pbar:
        sql = "UPDATE districts SET border='{}' WHERE name like '{}' AND city_id={}"
        sql = sql.format(str(x['border']), str('%' + x['name'] + '%'), cityId)

        try:
            DB.insetBorderIntoDistrict(sql)
            pbar.set_description(x['name'] + '已导入')
        except:
            pbar.set_description(x['name'] + '导入失败')


# 获取在区里面商圈的二手房价格
def saveBizcircleIntoDB(city):
    cityId = DB.getCityId(city)
    areaList = DB.getDistricts(city)

    for x in areaList:
        print(x['name'])
        lat = []
        lng = []
        for y in x['border'].split(';'):
            lng.append(float(y.split(',')[0]))
            lat.append(float(y.split(',')[1]))
        li = []
        step = 0.02
        for x in numpy.arange(min(lng), max(lng), step):
            for y in numpy.arange(min(lat), max(lat), step):
                li.append((round(y, 6), round(y - step, 6), round(x, 6), round(x - step, 6)))
        pbar = tqdm.tqdm(li)

        for x in pbar:
            try:
                ret = Lianjia(city).getBizcircleInfo(x[0], x[1], x[2], x[3])
                DB.insertIntoHousePrices(ret, cityId)
            except:
                pass



if __name__ == '__main__':
    city = '杭州'
    # saveDistrictBorderIntoDB(city)
    # saveBizcircleIntoDB(city)  # 下载城市区域数据

