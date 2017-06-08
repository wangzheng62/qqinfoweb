import pymssql,time
def dologin(loginname,passwd):
	try:
		conn=pymssql.connect('127.0.0.1','sa','12345678')
		cr=conn.cursor()
		sql01='select loginname,endtime,auth,creator from manager.dbo.userlist where loginname=\'%s\' and passwd=%s;'%(loginname,passwd)
		cr.execute(sql01)
		t1=cr.fetchone()
		print('t1',t1[1])
		today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
		if t1[1]<today:
			print('时间问题')
			t=None
		else:
			sql02='select contact from manager.dbo.userlist where loginname=\'%s\';'%t1[3]
			#print(sql02)
			#print('时间没问题',t1)
			cr.execute(sql02)
			t2=cr.fetchone()
			t1=list(t1)
			t1.append(t2[0])
			t=t1
			#t=(%loginname,%endtime,%auth,%creator,%contactofcreator)
		return t
	except Exception as e:
		print(e)
		pass
#管理页初始化
def getuserlist(loginname,creator):
	l=[('编号','登录名','密码','到期时间','权限等级','所属管理员','联系方式')]
	conn=pymssql.connect('127.0.0.1','sa','12345678')
	cr=conn.cursor()
	if loginname=='admin':
		sql='select * from  manager.dbo.userlist order by endtime ;'
	else:
		sql='select * from  manager.dbo.userlist where creator=\'%s\' order by endtime ;'%loginname
	cr.execute(sql)
	rows=cr.fetchall()
	l[len(l):len(l)]=rows
	return l

#管理员功能		
def adduser(*args):
	try:
		conn=pymssql.connect('127.0.0.1','sa','12345678')
		cr=conn.cursor()
		t=tuple(args)
		s=str(t)
		sql='insert into manager.dbo.userlist values %s;'%s
		print(sql)
		cr.execute(sql)
		conn.commit()
		return True
	except Exception:
		return False
def updateuser(*args):
	try:
		conn=pymssql.connect('127.0.0.1','sa','12345678')
		cr=conn.cursor()
		#t=tuple(args)
		#s=str(t)
		sql='update manager.dbo.userlist set passwd=\'%s\',endtime=\'%s\',contact=\'%s\' where loginname=\'%s\';'%(args[1],args[2],args[3],args[0])
		print(sql)
		cr.execute(sql)
		conn.commit()
		return True
	except Exception as e:
		print(e)
		return False
def deluser(*args):
	try:
		conn=pymssql.connect('127.0.0.1','sa','12345678')
		cr=conn.cursor()
		#t=tuple(args)
		#s=str(t)
		sql='delete from manager.dbo.userlist where loginname=\'%s\' and creator=\'%s\';'%(args[0],args[1])
		print(sql)
		cr.execute(sql)
		conn.commit()
		return True
	except Exception:
		return False

if __name__=='__main__':	
	adduser(*['admin','123456','2099-12-30','qqq'])