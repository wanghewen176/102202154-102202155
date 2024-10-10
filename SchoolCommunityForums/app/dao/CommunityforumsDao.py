from ..common import mysqlHelper
from ..model import Communityforums 
from ..dao import UsersDao
class CommunityforumsDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()


	def insert(self,datas):
		sql = "insert into communityforums (UsersId,path,Title,Content,PublichTime) value('" + str(datas.UsersId) +"','" + str(datas.path) +"','" + str(datas.Title) +"','" + str(datas.Content) +"','" + str(datas.PublichTime) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def update(self,datas):
		sql = "UPDATE communityforums SET UsersId='"+str(datas.UsersId)+"',path='"+str(datas.path)+"',Title='"+str(datas.Title)+"',Content='"+str(datas.Content)+"',PublichTime='"+str(datas.PublichTime)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete(self,id):
		sql = "DELETE FROM communityforums WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def select_all(self):
		sql    = "select * from communityforums";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumsdao_entity = Communityforums.Communityforums()
				communityforumsdao_entity.Id = str(row[0])
				communityforumsdao_entity.UsersId = str(row[1])
				communityforumsdao_entity.path = str(row[2])
				communityforumsdao_entity.Title = str(row[3])
				communityforumsdao_entity.Content = str(row[4])
				communityforumsdao_entity.PublichTime = str(row[5])
				lists.append(communityforumsdao_entity)
			self.mysqlutil.end()
		return lists

	def select_single(self,id):
		sql    = "select * from communityforums where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		communityforumsdao_entity = None
		if result > 0:
			communityforumsdao_entity = Communityforums.Communityforums()
			for row in self.mysqlutil.cursor.fetchall():
				communityforumsdao_entity.Id = str(row[0])
				communityforumsdao_entity.UsersId = str(row[1])
				communityforumsdao_entity.Users   = UsersDao.UsersDao().select_single(str(row[1]))				
				communityforumsdao_entity.path = str(row[2])
				communityforumsdao_entity.Title = str(row[3])
				communityforumsdao_entity.Content = str(row[4])
				communityforumsdao_entity.PublichTime = str(row[5])
			self.mysqlutil.end()
		return communityforumsdao_entity
	
	def select_all_by_userId(self,userId):
		sql    = "select * from communityforums where UsersId="+userId;
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumsdao_entity = Communityforums.Communityforums()
				communityforumsdao_entity.Id = str(row[0])
				communityforumsdao_entity.UsersId = str(row[1])
				communityforumsdao_entity.path = str(row[2])
				communityforumsdao_entity.Title = str(row[3])
				communityforumsdao_entity.Content = str(row[4])
				communityforumsdao_entity.PublichTime = str(row[5])
				lists.append(communityforumsdao_entity)
			self.mysqlutil.end()
		return lists
	
	def select_all_by_communityForumsId(self,communityForumsId):
		sql    = "select * from communityforums where UsersId="+communityForumsId;
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumsdao_entity = Communityforums.Communityforums()
				communityforumsdao_entity.Id = str(row[0])
				communityforumsdao_entity.UsersId = str(row[1])
				communityforumsdao_entity.path = str(row[2])
				communityforumsdao_entity.Title = str(row[3])
				communityforumsdao_entity.Content = str(row[4])
				communityforumsdao_entity.PublichTime = str(row[5])
				lists.append(communityforumsdao_entity)
			self.mysqlutil.end()
		return lists

