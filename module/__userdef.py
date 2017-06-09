class UserMetaclass(type):
	def __new__(cls,name,*args):
		
	
class User():
	__type=''
	def __init__(self,username,**kw):
		self.username=username
		for key in kw:
			if key=='loginname':
				continue
			else:
				exec('self.%s=kw[key]'%key)
if __name__=='__main__':
	u=User('test')
	print(u.username)
