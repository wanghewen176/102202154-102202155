from ..common import mysqlHelper
from ..model import Admins


class AdminsDao(object):
    def __init__(self):
        self.mysqlutil = mysqlHelper.MySqlHelper()

    def insert(self, datas):
        sql = "insert into admins (UserName,UserPWD) value('" + str(datas.UserName) + "','" + str(datas.UserPWD) + "');"
        self.mysqlutil.query(sql, "")
        self.mysqlutil.connent.commit()
        self.mysqlutil.end()

    def update(self, datas):
        sql = "UPDATE admins SET UserName='" + str(datas.UserName) + "',UserPWD='" + str(
            datas.UserPWD) + "' WHERE Id=" + str(datas.Id) + ";"
        self.mysqlutil.query(sql, "")
        self.mysqlutil.connent.commit()
        self.mysqlutil.end()

    def delete(self, id):
        sql = "DELETE FROM admins WHERE Id=" + str(id) + ";"
        self.mysqlutil.query(sql, "")
        self.mysqlutil.connent.commit()
        self.mysqlutil.end()

    def select_all(self):
        sql = "select * from admins";
        result = self.mysqlutil.query(sql, "")
        lists = []
        if result > 0:
            for row in self.mysqlutil.cursor.fetchall():
                adminsdao_entity = Admins.Admins()
                adminsdao_entity.Id = str(row[0])
                adminsdao_entity.UserName = str(row[1])
                adminsdao_entity.UserPWD = str(row[2])
                lists.append(adminsdao_entity)
            self.mysqlutil.end()
        return lists

    def select_single(self, id):
        sql = "select * from admins where id = " + str(id) + ";"
        result = self.mysqlutil.query(sql, "")
        adminsdao_entity = Admins.Admins()
        if result > 0:
            for row in self.mysqlutil.cursor.fetchall():
                adminsdao_entity.Id = str(row[0])
                adminsdao_entity.UserName = str(row[1])
                adminsdao_entity.UserPWD = str(row[2])
            self.mysqlutil.end()
        return adminsdao_entity

    def check_login(self, username, pwd):
        sql = "select * from admins where UserName='" + str(username) + "' and UserPWD='" + str(pwd) + "';"
        result = self.mysqlutil.query(sql, "")
        adminsdao_entity = None
        if result > 0:
            adminsdao_entity = Admins.Admins()
            for row in self.mysqlutil.cursor.fetchall():
                adminsdao_entity.Id = str(row[0])
                adminsdao_entity.UserName = str(row[1])
                adminsdao_entity.UserPWD = str(row[2])
            self.mysqlutil.end()
        return adminsdao_entity
