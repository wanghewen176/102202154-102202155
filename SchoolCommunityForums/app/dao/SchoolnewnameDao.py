
from ..common import mysqlHelper
from ..model import Schoolnewname 
class SchoolnewnameDao(object):
	def __init__(self):
		self.mysqlutil = mysqlHelper.MySqlHelper()


	def insert(self,datas):
		sql = "insert into schoolnewname (SchoolNewPath,SchoolNewName,SchoolNewContent,PublichTime) value('" + str(datas.SchoolNewPath) +"','" + str(datas.SchoolNewName) +"','" + str(datas.SchoolNewContent) +"','" + str(datas.PublichTime) +"');"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def update(self,datas):
		sql = "UPDATE schoolnewname SET SchoolNewPath='"+str(datas.SchoolNewPath)+"',SchoolNewName='"+str(datas.SchoolNewName)+"',SchoolNewContent='"+str(datas.SchoolNewContent)+"',PublichTime='"+str(datas.PublichTime)+"' WHERE Id="+str(datas.Id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def delete(self,id):
		sql = "DELETE FROM schoolnewname WHERE Id="+str(id)+";"
		self.mysqlutil.query(sql, "")
		self.mysqlutil.connent.commit()
		self.mysqlutil.end()


	def select_all(self):
		sql    = "select * from schoolnewname";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				schoolnewnamedao_entity = Schoolnewname.Schoolnewname()
				schoolnewnamedao_entity.Id = str(row[0])
				schoolnewnamedao_entity.SchoolNewPath = str(row[1])
				schoolnewnamedao_entity.SchoolNewName = str(row[2])
				schoolnewnamedao_entity.SchoolNewContent = str(row[3])
				schoolnewnamedao_entity.PublichTime = str(row[4])
				lists.append(schoolnewnamedao_entity)
			self.mysqlutil.end()
		return lists
	

	def select_all_by_keywords(self,keywords):
		sql    = "select * from schoolnewname WHERE SchoolNewName LIKE '%"+keywords+"%' or SchoolNewContent LIKE '%"+keywords+"%'";
		result =  self.mysqlutil.query(sql, "")
		lists  = []
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				schoolnewnamedao_entity = Schoolnewname.Schoolnewname()
				schoolnewnamedao_entity.Id = str(row[0])
				schoolnewnamedao_entity.SchoolNewPath = str(row[1])
				schoolnewnamedao_entity.SchoolNewName = str(row[2])
				schoolnewnamedao_entity.SchoolNewContent = str(row[3])
				schoolnewnamedao_entity.PublichTime = str(row[4])
				lists.append(schoolnewnamedao_entity)
			self.mysqlutil.end()
		return lists



	def select_single(self,id):
		sql    = "select * from schoolnewname where id = "+ str(id)+";"
		result =  self.mysqlutil.query(sql, "")
		schoolnewnamedao_entity = Schoolnewname.Schoolnewname()
		if result > 0:
			for row in self.mysqlutil.cursor.fetchall():
				schoolnewnamedao_entity.Id = str(row[0])
				schoolnewnamedao_entity.SchoolNewPath = str(row[1])
				schoolnewnamedao_entity.SchoolNewName = str(row[2])
				schoolnewnamedao_entity.SchoolNewContent = str(row[3])
				schoolnewnamedao_entity.PublichTime = str(row[4])
			self.mysqlutil.end()
		return schoolnewnamedao_entity
