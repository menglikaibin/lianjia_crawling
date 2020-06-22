import pymysql
import time
import GD


class DB:
    def __init__(self, host='127.0.0.1', port=3306, db='lianjia', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


# 获取城市信息
def getCityInfo(cityName):
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        sql = "select * from cities where name=%s OR name=%s"
        db.execute(sql, (cityName + '市', cityName + '州'))

    city = db.fetchone()

    return city


# 获取所有有边界的区
def getDistricts():
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        sql = "select * from districts where border is not null"
        db.execute(sql)

    return db.fetchall()


# 获取城市id
def getCityId(cityName):
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        sql = "select * from cities where name=%s OR name=%s"
        db.execute(sql, (cityName + '市', cityName + '州'))

    city = db.fetchone()

    return city['id']


# 插入区的边界经纬度
def insetBorderIntoDistrict(sql):
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        db.execute(sql)


# 获取某个市下面的区
def getDistricts(city):
    cityId = getCityId(city)

    sql = "SELECT * FROM districts WHERE city_id={} AND border IS NOT NULL"
    sql = sql.format(cityId)

    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        db.execute(sql)

    return db.fetchall()


# 获取区
def getDistrictByName(cityId, districtName):
    sql = "SELECT * FROM districts WHERE city_id={} AND (name='{}' OR name='{}')"
    sql = sql.format(cityId, districtName + '区', districtName + '县')

    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        db.execute(sql)

    return db.fetchone()


# 插入房价数据
def insertIntoHousePrices(ret, city):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        if ret is not None:
            for i in ret:
                print(i['name'])
                db.execute("SELECT * FROM house_prices WHERE `sign`={}".format(i['id']))
                res = db.fetchall()
                if (len(res) == 0):
                    sql = "INSERT INTO house_prices (`type`, `name`, `city_id`, `city_name`, `sign`, `baidu_lng`, `baidu_lat`, `unit_price`, `count`, `created_at`, `updated_at`) values (1, '{}', {}, '{}', {}, '{}', '{}', {}, {}, '{}', '{}')"
                    sql = sql.format(i['name'], city['id'], city['name'], i['id'], i['longitude'], i['latitude'], i['unit_price'], i['count'], now, now)
                    db.execute(sql)


# 转换高德经纬度
def changeBaiduToGaode():
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        db.execute("SELECT * FROM house_prices WHERE gaode_lat IS NULL")

    res = db.fetchall()

    count = 0
    for i in res:
        location = GD.getGaodeLocation(i['baidu_lat'], i['baidu_lng'])
        locationList = location.split(',')

        with DB() as db:
            sql = "UPDATE house_prices SET gaode_lng='{}', gaode_lat='{}' WHERE id={}"
            sql = sql.format(locationList[0], locationList[1], i['id'])
            db.execute(sql)

        # time.sleep(0.5)
        count += 1
        print(count)


# 插入城市房价
def insertCityHousePrice(name, price):
    with DB(host='192.168.0.197', user='LocationApp', passwd='123456', db='linhuiba3.1') as db:
        sql = "UPDATE cities SET house_price={} WHERE `name` like '%{}%'"
        sql = sql.format(price, name)
        db.execute(sql)

# 插入房价数据
def insertXiaoqu(ret, city):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        if ret is not None:
            for i in ret:
                print(i['name'])
                db.execute("SELECT * FROM house_prices WHERE `sign`={}".format(i['id']))
                res = db.fetchall()
                if (len(res) == 0):
                    sql = "INSERT INTO xiaoqu (`type`, `name`, `city_id`, `city_name`, `sign`, `baidu_lng`, `baidu_lat`, `unit_price`, `count`, `created_at`, `updated_at`) values (1, '{}', {}, '{}', {}, '{}', '{}', {}, {}, '{}', '{}')"
                    sql = sql.format(i['name'], city['id'], city['name'], i['id'], i['longitude'], i['latitude'], i['unit_price'], i['count'], now, now)
                    db.execute(sql)


if __name__ == '__main__':
    insetBorderIntoDistrict('杭州市')
