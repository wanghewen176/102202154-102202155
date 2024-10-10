from ..common import mysqlHelper
from ..model import Communityforumscomments 
from ..dao import UsersDao
class CommunityforumscommentsDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()


	def insert(self,datas):
		sql = "insert into communityforumscomments (UsersId,CommunityForumsId,CommentsContent,CommentsTime) value('" + str(datas.UsersId) +"','" + str(datas.CommunityForumsId) +"','" + str(datas.CommentsContent) +"','" + str(datas.CommentsTime) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def update(self,datas):
		sql = "UPDATE communityforumscomments SET UsersId='"+str(datas.UsersId)+"',CommunityForumsId='"+str(datas.CommunityForumsId)+"',CommentsContent='"+str(datas.CommentsContent)+"',CommentsTime='"+str(datas.CommentsTime)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete(self,id):
		sql = "DELETE FROM communityforumscomments WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def select_all(self):
		sql    = "select * from communityforumscomments";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumscommentsdao_entity = Communityforumscomments.Communityforumscomments()
				communityforumscommentsdao_entity.Id = str(row[0])
				communityforumscommentsdao_entity.UsersId = str(row[1])

				communityforumscommentsdao_entity.Users   = UsersDao().select_single(str(row[1]))				

				communityforumscommentsdao_entity.CommunityForumsId = str(row[2])
				communityforumscommentsdao_entity.CommentsContent = str(row[3])
				communityforumscommentsdao_entity.CommentsTime = str(row[4])
				lists.append(communityforumscommentsdao_entity)
			self.mysqlutil.end()
		return lists
	

	def select_single(self,id):
		sql    = "select * from communityforumscomments where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		communityforumscommentsdao_entity = Communityforumscomments.Communityforumscomments()
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumscommentsdao_entity.Id = str(row[0])
				communityforumscommentsdao_entity.UsersId = str(row[1])
				
				communityforumscommentsdao_entity.Users   = UsersDao.UsersDao().select_single(str(row[1]))
				
				communityforumscommentsdao_entity.CommunityForumsId = str(row[2])
				communityforumscommentsdao_entity.CommentsContent = str(row[3])
				communityforumscommentsdao_entity.CommentsTime = str(row[4])
			self.mysqlutil.end()
		return communityforumscommentsdao_entity


	def select_all_by_community_id(self, ids):
		sql    = "select * from communityforumscomments where CommunityForumsId="+str(ids);
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumscommentsdao_entity = Communityforumscomments.Communityforumscomments()
				communityforumscommentsdao_entity.Id = str(row[0])
				communityforumscommentsdao_entity.UsersId = str(row[1])

				communityforumscommentsdao_entity.Users   = UsersDao.UsersDao().select_single(str(row[1]))				

				communityforumscommentsdao_entity.CommunityForumsId = str(row[2])
				communityforumscommentsdao_entity.CommentsContent = str(row[3])
				communityforumscommentsdao_entity.CommentsTime = str(row[4])
				lists.append(communityforumscommentsdao_entity)
			self.mysqlutil.end()
		return lists


	def select_all_by_users_id(self, ids):
		sql    = "select * from communityforumscomments where UsersId="+str(ids);
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				communityforumscommentsdao_entity = Communityforumscomments.Communityforumscomments()
				communityforumscommentsdao_entity.Id = str(row[0])
				communityforumscommentsdao_entity.UsersId = str(row[1])

				communityforumscommentsdao_entity.Users   = UsersDao.UsersDao().select_single(str(row[1]))				

				communityforumscommentsdao_entity.CommunityForumsId = str(row[2])
				communityforumscommentsdao_entity.CommentsContent = str(row[3])
				communityforumscommentsdao_entity.CommentsTime = str(row[4])
				lists.append(communityforumscommentsdao_entity)
			self.mysqlutil.end()
		return lists