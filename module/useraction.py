import pymssql,time,os
#数据设置
def getconn():
	SEVERCONFIG=['127.0.0.1','sa','12345678']
	conn=pymssql.connect(*SEVERCONFIG)
	return conn
#登录
def dologin(loginname,passwd,conn=getconn()):
	try:
		error=''
		logininfo=[]
		cr=conn.cursor()
		#在用户列表里验证账号密码
		sql01='select loginname,endtime,auth,creator from manager.dbo.userlist where loginname=\'%s\' and passwd=\'%s\';'%(loginname,passwd)
		cr.execute(sql01)
		t1=cr.fetchone()
		if t1==None:#账号密码不匹配
			error='账号或密码错误'
			logininfo.append(error)
			return logininfo
		else :#账号密码匹配，验证日期
			today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
			if t1[1]<today:#过期账号
				error='账号过期请联系客服'
				logininfo.append(error)
				return logininfo
			else:#账户合格，查询登录情况
			#在登录列表里查找登录状态
				sql02='select loginname,logintime from manager.dbo.onlinelist where loginname=\'%s\';'%loginname
				cr.execute(sql02)
				t2=cr.fetchone()
				now=time.time()
				if not t2==None :#已经登陆
					if (now-t2[1])<600:#登陆时间少于10分钟
						error='账号已经登录'
						logininfo.append(error)
						return logininfo
					else:#超过默认登录时间
						delonline(loginname)
						logininfo.append(error)
						for s in t1:
							logininfo.append(s)
						logininfo.append(now)
					#在登录列表里插入登录记录
						insertonline(loginname,now)
						return logininfo
				else:#没有
					logininfo.append(error)
					for s in t1:
						logininfo.append(s)
					logininfo.append(now)
					insertonline(loginname,now)
					return logininfo	

	except Exception as e:
		raise e
		logininfo=[]
		error='未知错误'
		logininfo.append(error)
		return logininfo
#插入登录信息
def insertonline(loginname,logintime,conn=getconn()):
	cr=conn.cursor()
	sql='insert into manager.dbo.onlinelist values (\'%s\',%s);'%(loginname,logintime)
	#print(sql)
	cr.execute(sql)
	conn.commit()

#删除登录信息
def delonline(loginname,conn=getconn()):
	cr=conn.cursor()
	sql='delete from manager.dbo.onlinelist where loginname=\'%s\';'%loginname
	print(sql)
	cr.execute(sql)
	conn.commit()
#登出
#管理页初始化
def getuserlist(loginname,creator,conn=getconn()):
	l=[('编号','登录名','密码','到期时间','权限等级','所属管理员','联系方式')]
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
def adduser(*args,conn=getconn()):
	try:
		print(conn)
		cr=conn.cursor()
		t=tuple(args)
		s=str(t)
		sql='insert into manager.dbo.userlist values %s;'%s
		print(sql)
		cr.execute(sql)
		conn.commit()
		return True
	except Exception as e:
		print(e)
		return False
def updateuser(*args,conn=getconn()):
	try:
		cr=conn.cursor()
		#t=tuple(args)
		#s=str(t)
		sql='update manager.dbo.userlist set passwd=\'%s\',endtime=\'%s\',contact=\'%s\' where loginname=\'%s\';'%(args[1],args[2],args[3],args[0])
		#print(sql)
		cr.execute(sql)
		conn.commit()
		return True
	except Exception as e:
		print(e)
		return False
def deluser(*args,conn=getconn()):
	try:
		cr=conn.cursor()
		#t=tuple(args)
		#s=str(t)
		sql='delete from manager.dbo.userlist where loginname=\'%s\' and creator=\'%s\';'%(args[0],args[1])
		#print(sql)
		cr.execute(sql)
		conn.commit()
		return True
	except Exception:
		return False

if __name__=='__main__':	
	adduser(*['admin','123456','2099-12-30','qqq'])