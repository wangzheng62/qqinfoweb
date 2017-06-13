from module.__mssqlmetaclass import MssqlDb,MssqlTable
class Manager(MssqlDb):
	pass
		
class Userlist(MssqlTable,Manager):
	pass
class Onlinelist(MssqlTable,Manager):
	pass
#检测条件
def login(user):
	if user.isexist():
		return True
	else:
		return False
def auth(user):
	if user.getkw()['auth'][0]==2:
		return True
	else:
		return False
def date(user):
	if user.getkw()['endtime'][0]=='2017-07-01':
		return True
	else:
		return False
def err(n):
	return '条件%s失败'%n