
from ..common import mysqlHelper
from ..model import Schoolnewcomments 
from ..dao import UsersDao
class SchoolnewcommentsDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()


	def insert(self,datas):
		sql = "insert into schoolnewcomments (UsersId,SchoolNewId,CommentsContent,CommentsTime) value('" + str(datas.UsersId) +"','" + str(datas.SchoolNewId) +"','" + str(datas.CommentsContent) +"','" + str(datas.CommentsTime) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def update(self,datas):
		sql = "UPDATE schoolnewcomments SET UsersId='"+str(datas.UsersId)+"',SchoolNewId='"+str(datas.SchoolNewId)+"',CommentsContent='"+str(datas.CommentsContent)+"',CommentsTime='"+str(datas.CommentsTime)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete_by_schoolnew_id(self,SchoolNewId):
		sql = "DELETE FROM schoolnewcomments WHERE SchoolNewId="+str(SchoolNewId)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete(self,id):
		sql = "DELETE FROM schoolnewcomments WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def select_all(self):
		sql    = "select * from schoolnewcomments";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				schoolnewcommentsdao_entity = Schoolnewcomments.Schoolnewcomments()
				schoolnewcommentsdao_entity.Id = str(row[0])
				schoolnewcommentsdao_entity.UsersId = str(row[1])
				schoolnewcommentsdao_entity.SchoolNewId = str(row[2])
				schoolnewcommentsdao_entity.CommentsContent = str(row[3])
				schoolnewcommentsdao_entity.CommentsTime = str(row[4])
				lists.append(schoolnewcommentsdao_entity)
			self.mysqlutil.end()
		return lists

	def select_single(self,id):
		sql    = "select * from schoolnewcomments where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		schoolnewcommentsdao_entity = Schoolnewcomments.Schoolnewcomments()
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				schoolnewcommentsdao_entity.Id = str(row[0])
				schoolnewcommentsdao_entity.UsersId = str(row[1])
				schoolnewcommentsdao_entity.SchoolNewId = str(row[2])
				schoolnewcommentsdao_entity.CommentsContent = str(row[3])
				schoolnewcommentsdao_entity.CommentsTime = str(row[4])
			self.mysqlutil.end()
		return schoolnewcommentsdao_entity


	def select_all_by_schoolnew_id(self,ids):
		sql    = "select * from schoolnewcomments where SchoolNewId="+str(ids);
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				schoolnewcommentsdao_entity = Schoolnewcomments.Schoolnewcomments()
				schoolnewcommentsdao_entity.Id = str(row[0])
				schoolnewcommentsdao_entity.UsersId = str(row[1])
				schoolnewcommentsdao_entity.Users = UsersDao.UsersDao().select_single(str(row[1]))
				
				schoolnewcommentsdao_entity.SchoolNewId = str(row[2])
				schoolnewcommentsdao_entity.CommentsContent = str(row[3])
				schoolnewcommentsdao_entity.CommentsTime = str(row[4])
				lists.append(schoolnewcommentsdao_entity)
			self.mysqlutil.end()
		return lists

