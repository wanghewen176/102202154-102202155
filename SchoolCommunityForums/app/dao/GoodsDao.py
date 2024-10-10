from ..common import mysqlHelper
from ..model import Goods 
from ..dao import UsersDao
class GoodsDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()


	def insert(self,datas):
		sql = "insert into goods (UsersId,GoodsPath,GoodsName,GoodsDetail,GoodsPrices,PublichTime) value('" + str(datas.UsersId) +"','" + str(datas.GoodsPath) +"','" + str(datas.GoodsName) +"','" + str(datas.GoodsDetail) +"','" + str(datas.GoodsPrices) +"','" + str(datas.PublichTime) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def update(self,datas):
		sql = "UPDATE goods SET UsersId='"+str(datas.UsersId)+"',GoodsPath='"+str(datas.GoodsPath)+"',GoodsName='"+str(datas.GoodsName)+"',GoodsDetail='"+str(datas.GoodsDetail)+"',GoodsPrices='"+str(datas.GoodsPrices)+"',PublichTime='"+str(datas.PublichTime)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete(self,id):
		sql = "DELETE FROM goods WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def select_all(self):
		sql    = "select * from goods";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				goodsdao_entity = Goods.Goods()
				goodsdao_entity.Id = str(row[0])
				goodsdao_entity.UsersId = str(row[1])		
				
				goodsdao_entity.Users  =UsersDao.UsersDao().select_single(str(row[1]))
				
				goodsdao_entity.GoodsPath = str(row[2])
				goodsdao_entity.GoodsName = str(row[3])
				goodsdao_entity.GoodsDetail = str(row[4])
				goodsdao_entity.GoodsPrices = str(row[5])
				goodsdao_entity.PublichTime = str(row[6])
				lists.append(goodsdao_entity)
			self.mysqlutil.end()
		return lists
	

	def select_single(self,id):
		sql    = "select * from goods where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		goodsdao_entity = None
		if result > 0:
			goodsdao_entity = Goods.Goods()
			for row in self.mysqlutil.cursor.fetchall():
				goodsdao_entity.Id = str(row[0])
				goodsdao_entity.UsersId = str(row[1])
				goodsdao_entity.Users  =UsersDao.UsersDao().select_single(str(row[1]))				

				goodsdao_entity.GoodsPath = str(row[2])
				goodsdao_entity.GoodsName = str(row[3])
				goodsdao_entity.GoodsDetail = str(row[4])
				goodsdao_entity.GoodsPrices = str(row[5])
				goodsdao_entity.PublichTime = str(row[6])
			self.mysqlutil.end()
		return goodsdao_entity


	def select_all_by_userId(self,userId):
		sql    = "select * from goods where UsersId="+str(userId);
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				goodsdao_entity = Goods.Goods()
				goodsdao_entity.Id          = str(row[0])
				goodsdao_entity.UsersId     = str(row[1])
				
				goodsdao_entity.Users  =UsersDao.UsersDao().select_single(str(row[1]))				

				goodsdao_entity.GoodsPath   = str(row[2])
				goodsdao_entity.GoodsName   = str(row[3])
				goodsdao_entity.GoodsDetail = str(row[4])
				goodsdao_entity.GoodsPrices = str(row[5])
				goodsdao_entity.PublichTime = str(row[6])
				lists.append(goodsdao_entity)
			self.mysqlutil.end()
		return lists