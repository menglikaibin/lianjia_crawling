import pymysql

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


def getCities(cityName):
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        sql = "select * from cities where name=%s"
        db.execute(sql, (cityName + '市'))

        for i in db:
            print(i['id'])

    return i['id']


def insetBorderIntoDistrict(sql):
    with DB(host='127.0.0.1', user='root', passwd='root', db='lianjia') as db:
        db.execute(sql)


if __name__ == '__main__':
    insetBorderIntoDistrict('杭州市')
