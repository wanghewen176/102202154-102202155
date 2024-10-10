import json

class Users(object): 
  
	"""description of class"""
	def __init__(self):
		self.Id = None
		self.UserName = None
		self.PWD = None
		self.Name = None
		self.Phone = None
		self.Card = None
		self.StudentClass = None
		self.Address = None

	def users_encoder(self,obj):
		if isinstance(obj,Users):
			return {'Id':obj.Id,'UserName':obj.UserName,'PWD':obj.PWD,'Name':obj.Name,'Phone':obj.Phone,'Card':obj.Card,'StudentClass':obj.StudentClass,'Address':obj.Address,}
		return json.JSONEncoder.default(self,obj)
	
	def users_decoder(self,obj):
		users = None
		try:
			users          = Users()
			users.Id       = obj['Id']
			users.UserName      = obj['UserName']
			users.PWD	   = obj['PWD']
			users.Name     = obj['Name']
			users.Phone     = obj['Phone']
			users.Card	      = obj['Card']
			users.StudentClass = obj['StudentClass']
			users.Address        = obj['Address']
			
		except :
			return None
		return users