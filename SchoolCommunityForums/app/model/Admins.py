import json


class Admins(object):
    """description of class"""

    def __init__(self):
        self.Id = None
        self.UserName = None
        self.UserPWD = None

    def admin_encoder(self, obj):
        if isinstance(obj, Admins):
            return {'Id': obj.Id, 'UserName': obj.UserName, 'UserPWD': obj.UserPWD, }
        return json.JSONEncoder.default(self, obj)

    def admin_decoder(self, obj):
        admins = None
        try:
            admins = Admins()
            admins.Id = obj['Id']
            admins.UserName = obj['UserName']
            admins.UserPWD = obj['UserPWD']
        except:
            return None
        return admins
