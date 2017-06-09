
import pymssql,time
from __sqlstatement import USERLIST,ONLINELIST
from __userdef import User
#数据设置
def getconn():
	SEVERCONFIG=['127.0.0.1','sa','12345678']
	conn=pymssql.connect(*SEVERCONFIG)
	return conn
#账号密码检查，获取账号信息
def getuser(loginname,passwd):
	conn=getconn()
	cr=conn.cursor()
	#在用户列表里验证账号密码
	sql=USERLIST['获取用户信息']%(loginname,passwd)
	cr.execute(sql)
	t=cr.fetchone()
	if t==None:#账号密码不匹配
		return False
	else:
		sql01=USERLIST['获取列名']
		cr.execute(sql01)
		t1=cr.fetchall()
		t2=[]
		for row in t1:
			t2.append(row[0])
		#组合成dict，创建user
		d=dict(zip(t2,t))
		user=User(loginname,**d)
		return user
#账号信息检查		
def timecheck(user):
	today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
	if user.endtime<today:#过期账号
		error='账号过期请联系客服'
		return False
	else:
		return True
def authcheck(user):
	pass
#状态检测
def logtimecheck(user):
	pass
def pointcheck(user):
	pass
if __name__=='__main__':
	user=getuser('test','12345678')
	