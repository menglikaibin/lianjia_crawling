import pymysql
import time


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

    sql = "SELECT * FROM districts WHERE city_id={}"
    sql = sql.format(cityId)

    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        db.execute(sql)

    return db.fetchall()


# 插入房价数据
def insertIntoHousePrices(ret, cityId):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        if ret is not None:
            for i in ret:
                print(i['name'])
                db.execute("SELECT * FROM house_prices WHERE `sign`={}".format(i['id']))
                res = db.fetchall()
                if (len(res) == 0):
                    sql = "INSERT INTO house_prices (`type`, `name`, `city_id`, `sign`, `baidu_lng`, `baidu_lat`, `unit_price`, `count`, `created_at`, `updated_at`) values (1, '{}', {}, {}, '{}', '{}', {}, {}, {}, {})"
                    sql = sql.format(i['name'], cityId, i['id'], i['longitude'], i['latitude'], i['unit_price'], i['count'], now, now)
                    db.execute(sql)


if __name__ == '__main__':
    insetBorderIntoDistrict('杭州市')
