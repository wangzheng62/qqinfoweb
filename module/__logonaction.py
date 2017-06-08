'''
			else:#账户合格，查询登录情况
			#在登录列表里查找登录状态
				
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
		return logininfo'''
import pymssql
#数据设置
def getconn():
	SEVERCONFIG=['127.0.0.1','sa','12345678']
	conn=pymssql.connect(*SEVERCONFIG)
	return conn
#账号密码检查，获取账号信息
def passwdcheck(loginname,passwd):
	conn=getconn()
	cr=conn.cursor()
	#在用户列表里验证账号密码
	sql='select * from manager.dbo.userlist where loginname=\'%s\' and passwd=\'%s\';'%(loginname,passwd)
	cr.execute(sql)
	t=cr.fetchone()
	print('t:',t)
	if t==None:#账号密码不匹配
		error='账号或密码错误'
		return False
	else:
		sql01='''use manager;
				select name from syscolumns where id = object_id('dbo.userlist') order by colorder;'''
		cr.execute(sql01)
		t1=cr.fetchall()
		t2=[]
		for row in t1:
			t2.append(row[0])	
		d=dict(zip(t2,t))
		print(d)
#账号信息检查		
def timecheck(user):
	today=time.strftime('%Y-%m-%d',time.localtime(time.time()))8
	if user.endtime<today:#过期账号
		error='账号过期请联系客服'
		return False
	else:
		return True
def authcheck(user):
	pass
#状态检测
def logtimecheck(user):
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
	pass
def pointcheck(user):
	pass
if __name__=='__main__':
	passwdcheck('test','12345678')
	