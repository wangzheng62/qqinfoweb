import pymssql,time
#获取数据库连接
def getconn():
	SEVERCONFIG=['127.0.0.1','sa','12345678']
	conn=pymssql.connect(*SEVERCONFIG)	
	return conn
	
#查询QQ号
def queryqqnum(s):
	#变量初始化
	conn=getconn()
	cr=conn.cursor()
	l=[]
	i=1
	sql=''
	#查询语句生成
	while(i<=4):
		sql=sql+'select QQNum,Nick,Age,Qunnum from qq.dbo.group%s with(index(qqnum_index)) where qqnum=\'%s\' union all '%(i,s)
		i+=1		
	sql=sql[:-10]+';'
	#执行查询返回结果
	cr.execute(sql)
	t=cr.fetchall()
	#print('qq_',t)
	#添加群名称
	if t==None:
		pass
	else:
		for row in t:
			rowlist=list(row)
			quninfo=__queryquninfo(row[3])
			#print(1)
			if quninfo==None:
				rowlist.append('None')
				#print(2)
			else:
				try:
					rowlist.append(quninfo[1].encode('latin-1').decode('gbk'))
					#print(3)
				except Exception as e:
					#print(4,quninfo)
					#print(quninfo[1])
					#print(rowlist)
					rowlist.append(quninfo[1])
			#print(5)
			l.append(rowlist)
		#print(6)
		res=[]
		
		for row in l:
			ltemp=list(row)
			try:
				ltemp[1]=ltemp[1].encode('latin-1').decode('gbk')
			except Exception:
				pass
			res.append(ltemp)
			#print(l)
	#print('res_',res)
	return res
#查询QQ群
def queryqunnum(s):
	#start=time.time()
	l=[]
	if isinstance(s,int):
		s=str(s)
	s1=s[:-7]
	s2=s[:-5]
	if s1=='':
		s1=0
	s1=int(s1)+1
	s2=int(s2)+1
	sql='select QQNum,Nick,Age,Qunnum from groupdata%s.dbo.group%s where qunnum=%s'%(s1,s2,s)
	conn=getconn()
	cr=conn.cursor()
	cr.execute(sql)
	t=cr.fetchall()
	#print('qun_',t)
	#添加群名称
	if t==None:
		pass
	else:
		for row in t:
			rowlist=list(row)
			quninfo=__queryquninfo(row[3])
			#print(1)
			if quninfo==None:
				rowlist.append('None')
				#print(2)
			else:
				try:
					rowlist.append(quninfo[1].encode('latin-1').decode('gbk'))
					#print(3)
				except Exception as e:
					#print(4,quninfo)
					#print(quninfo[1])
					#print(rowlist)
					rowlist.append(quninfo[1])
			#print(5)
			l.append(rowlist)
		#print(6)
		res=[]
		for row in l:
			ltemp=list(row)
			try:
				ltemp[1]=ltemp[1].encode('latin-1').decode('gbk')
			except Exception:
				pass
			res.append(ltemp)
	return res
#查询群信息	
def __queryquninfo(s):
	conn=getconn()
	cr=conn.cursor()
	if isinstance(s,int):
		s=str(s)
	s1=s[:-7]
	if s1=='':
		s1=0
	s1=int(s1)+1
	s3=s[:-6]
	if s3=='':
		s3=0
	s3=int(s3)+1
	sql='select qunnum,title from quninfo%s.dbo.qunlist%s where qunnum=%s;'%(s1,s3,s)
	cr.execute(sql)
	t=cr.fetchone()
	#print('quninfo__',t)
	return t
	
#测试
if __name__=='__main__':
	pass