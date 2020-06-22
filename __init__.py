import lianjia as lj
import params
import time
import DB
import random


for i in params.city_dict:
    print(i)
    lj.saveDistrictBorderIntoDB(i)
    time.sleep(random.randint(1, 3))
# lj.saveDistrictBorderIntoDB('杭州')

# for i in params.direct_city_dict:
#     print(i)
#     lj.saveBizcircleIntoDB(i)
#     time.sleep(1)

# lj.saveBizcircleIntoDB('杭州')

# lj.getDistrictBizCircle('杭州', '余杭')

# 转换高德经纬度
# DB.changeBaiduToGaode()

