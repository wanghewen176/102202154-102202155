from ..common import mysqlHelper
from ..model import Goodscomments 
from ..dao import UsersDao
class GoodscommentsDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()


	def insert(self,datas):
		sql = "insert into goodscomments (UsersId,GoodsId,CommentsContent,CommentsTime) value('" + str(datas.UsersId) +"','" + str(datas.GoodsId) +"','" + str(datas.CommentsContent) +"','" + str(datas.CommentsTime) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def update(self,datas):
		sql = "UPDATE goodscomments SET UsersId='"+str(datas.UsersId)+"',GoodsId='"+str(datas.GoodsId)+"',CommentsContent='"+str(datas.CommentsContent)+"',CommentsTime='"+str(datas.CommentsTime)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete(self,id):
		sql = "DELETE FROM goodscomments WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def select_all(self):
		sql    = "select * from goodscomments";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				goodscommentsdao_entity = Goodscomments.Goodscomments()
				goodscommentsdao_entity.Id = str(row[0])
				goodscommentsdao_entity.UsersId = str(row[1])
				goodscommentsdao_entity.GoodsId = str(row[2])
				goodscommentsdao_entity.CommentsContent = str(row[3])
				goodscommentsdao_entity.CommentsTime = str(row[4])
				lists.append(goodscommentsdao_entity)
			self.mysqlutil.end()
		return lists

	def select_single(self,id):
		sql    = "select * from goodscomments where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		goodscommentsdao_entity = Goodscomments.Goodscomments()
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				goodscommentsdao_entity.Id = str(row[0])
				goodscommentsdao_entity.UsersId = str(row[1])
				goodscommentsdao_entity.GoodsId = str(row[2])
				goodscommentsdao_entity.CommentsContent = str(row[3])
				goodscommentsdao_entity.CommentsTime = str(row[4])
			self.mysqlutil.end()
		return goodscommentsdao_entity


	def select_all_by_user_id(self,userId):
		sql    = "select * from goodscomments where UsersId="+userId;
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				goodscommentsdao_entity = Goodscomments.Goodscomments()
				goodscommentsdao_entity.Id = str(row[0])
				goodscommentsdao_entity.UsersId = str(row[1])
				goodscommentsdao_entity.Users   = UsersDao.UsersDao().select_single(row[1])
				goodscommentsdao_entity.GoodsId = str(row[2])
				goodscommentsdao_entity.CommentsContent = str(row[3])
				goodscommentsdao_entity.CommentsTime = str(row[4])
				lists.append(goodscommentsdao_entity)
			self.mysqlutil.end()
		return lists
	

	def select_all_by_goods_id(self,goodsId):
		sql    = "select * from goodscomments where GoodsId="+goodsId;
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				goodscommentsdao_entity = Goodscomments.Goodscomments()
				goodscommentsdao_entity.Id = str(row[0])
				goodscommentsdao_entity.UsersId = str(row[1])
				goodscommentsdao_entity.Users   = UsersDao.UsersDao().select_single(row[1])
				goodscommentsdao_entity.GoodsId = str(row[2])
				goodscommentsdao_entity.CommentsContent = str(row[3])
				goodscommentsdao_entity.CommentsTime = str(row[4])
				lists.append(goodscommentsdao_entity)
			self.mysqlutil.end()
		return lists

