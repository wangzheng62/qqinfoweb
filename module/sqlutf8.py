import pymssql,time
#查询QQ号

def queryqqnum(s):
	
	conn=pymssql.connect('127.0.0.1','sa','12345678')
	cr=conn.cursor()
	#start=time.time()
	l=[]
	i=1
	sql=''
	while(i<=4):
		sql=sql+'select QQNum,Nick,Age,Qunnum from qq.dbo.group%s with(index(qqnum_index)) where qqnum=%s union all '%(i,s)
		i+=1		
	sql=sql[:-10]+';'
	print(sql)
	cr.execute(sql)
	t=cr.fetchall()
	print(t)
	#编码转换
	for row in t:
		ltemp=list(row)
		ltemp[1]=ltemp[1].encode('latin-1').decode('gbk')
		l.append(ltemp)
	#end=time.time()
	#print(end-start)
	return l
	
#查询QQ群
def queryqunnum(s):
	#start=time.time()
	l=[]
	try:
		if isinstance(s,int):
			s=str(s)
		s1=s[:-7]
		s2=s[:-5]
		s3=s[:-6]
		if s1=='':
			s1=0
		s1=int(s1)+1
		s2=int(s2)+1
		if s3=='':
			s3=0
		s3=int(s3)+1
		sql='select QQNum,Nick,Age,Qunnum from groupdata%s.dbo.group%s where qunnum=%s'%(s1,s2,s)
		sql01='select qunnum,title from quninfo%s.dbo.qunlist%s where qunnum=%s;'%(s1,s3,s)
		conn=pymssql.connect('127.0.0.1','sa','12345678')
		cr=conn.cursor()
		qunnum=s
		cr.execute(sql)
		t1=cr.fetchall()
		cr.execute(sql01)
		t2=cr.fetchone()
		if t1==None:
			pass
		else:
			if t2==None:
				t=[]
				for row in t1:
					row=list(row)
					row.append(None)
					t.append(row)
			else:
				t=[]
				for row in t1:
					row=list(row)
					row.append(t2[1].encode('latin-1').decode('gbk'))
					t.append(row)
		#编码转换
		for row in t:
			ltemp=list(row)
			ltemp[1]=ltemp[1].encode('latin-1').decode('gbk')
			l.append(ltemp)
	except Exception as e:
		print(e)
	##print(end-start)
	#print(l)
	return l