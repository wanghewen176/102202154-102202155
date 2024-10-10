import pymysql


class MySqlHelper(object):
    def __init__(self):
        self.connect_str = dict(host='127.0.0.1', port=3306, user='root', password='123456', database='schoolCommunity', charset='utf8')
        self.connent = pymysql.Connect(**self.connect_str)
        self.cursor = self.connent.cursor()
    
    def query(self,sql,parms):
        return self.cursor.execute(sql)

    #插入多个数据使用
    def query_more(self,sql,parms):
        return self.cursor.executemany(sql,parms)

    def end(self):
        self.cursor.close()
        self.connent.close()