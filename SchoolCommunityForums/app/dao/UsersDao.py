from ..common import mysqlHelper
from ..model import Users 
class UsersDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()

	def insert(self,datas):
		sql = "insert into users (UserName,PWD,Name,Phone,Card,StudentClass,Address) value('" + str(datas.UserName) +"','" + str(datas.PWD) +"','" + str(datas.Name) +"','" + str(datas.Phone) +"','" + str(datas.Card) +"','" + str(datas.StudentClass) +"','" + str(datas.Address) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()

	def update(self,datas):
		sql = "UPDATE users SET UserName='"+str(datas.UserName)+"',PWD='"+str(datas.PWD)+"',Name='"+str(datas.Name)+"',Phone='"+str(datas.Phone)+"',Card='"+str(datas.Card)+"',StudentClass='"+str(datas.StudentClass)+"',Address='"+str(datas.Address)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()
		
	def update_othing(self,datas):
		sql = "UPDATE users SET UserName='"+str(datas.UserName)+"',Name='"+str(datas.Name)+"',Phone='"+str(datas.Phone)+"',Card='"+str(datas.Card)+"',StudentClass='"+str(datas.StudentClass)+"',Address='"+str(datas.Address)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()

	def delete(self,id):
		sql = "DELETE FROM users WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()

	def select_all(self):
		sql    = "select * from users";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				usersdao_entity = Users.Users()
				usersdao_entity.Id = str(row[0])
				usersdao_entity.UserName = str(row[1])
				usersdao_entity.PWD = str(row[2])
				usersdao_entity.Name = str(row[3])
				usersdao_entity.Phone = str(row[4])
				usersdao_entity.Card = str(row[5])
				usersdao_entity.StudentClass = str(row[6])
				usersdao_entity.Address = str(row[7])
				lists.append(usersdao_entity)
			self.mysqlutil.end()
		return lists

	def select_single(self,id):
		sql    = "select * from users where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		usersdao_entity = Users.Users()
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				usersdao_entity.Id = str(row[0])
				usersdao_entity.UserName = str(row[1])
				usersdao_entity.PWD = str(row[2])
				usersdao_entity.Name = str(row[3])
				usersdao_entity.Phone = str(row[4])
				usersdao_entity.Card = str(row[5])
				usersdao_entity.StudentClass = str(row[6])
				usersdao_entity.Address = str(row[7])
			self.mysqlutil.end()
		return usersdao_entity

	def check_exist(self,userName):
		sql    = "select * from users where UserName='"+ str(userName)+"';"
		result =  self.mysqlutil.query(sql, "")
		usersdao_entity = None
		if result > 0:
			usersdao_entity = Users.Users()
			for row in self.mysqlutil.cursor.fetchall():
				usersdao_entity.Id = str(row[0])
				usersdao_entity.UserName = str(row[1])
				usersdao_entity.PWD = str(row[2])
				usersdao_entity.Name = str(row[3])
				usersdao_entity.Phone = str(row[4])
				usersdao_entity.Card = str(row[5])
				usersdao_entity.StudentClass = str(row[6])
				usersdao_entity.Address = str(row[7])
			self.mysqlutil.end()
		return usersdao_entity
	
	def check_login(self,userName,pwd):
		sql    = "select * from users where UserName='"+ str(userName)+"' and PWD='"+str(pwd)+"';"
		result =  self.mysqlutil.query(sql, "")
		usersdao_entity = None
		if result > 0:
			usersdao_entity = Users.Users()
			for row in self.mysqlutil.cursor.fetchall():
				usersdao_entity.Id = str(row[0])
				usersdao_entity.UserName = str(row[1])
				usersdao_entity.PWD = str(row[2])
				usersdao_entity.Name = str(row[3])
				usersdao_entity.Phone = str(row[4])
				usersdao_entity.Card = str(row[5])
				usersdao_entity.StudentClass = str(row[6])
				usersdao_entity.Address = str(row[7])
			self.mysqlutil.end()
		return usersdao_entity
	
