#！/usr/bin/env python3
#-*-coding -utf8 -*-
'router register'
from flask import Flask,render_template,session,request
from module import useraction,sql
import os,time
#变量初始化
app=Flask(__name__)
app.secret_key=os.urandom(24)
#页面注册

#导航页面
@app.route('/')
def index():
	return render_template('index.html')
#登录
@app.route('/indexlogin',methods=['get','post'])
def indexlogin():
	#print(session)
	namelist=['loginname','passwd']
	d=getpagedata(*namelist)
	if d['loginname']==session.get('loginname'):
		if session['auth']>2:
			return render_template('home.html',**session)
		else:
			return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),**session)
	#执行登录，返回登录信息[error,loginname,endtime,auth,creator,logintime]
	else:
		loginfo=useraction.dologin(d['loginname'],d['passwd'])
		if loginfo[0]=='':
			l=['error','loginname','endtime','auth','creator','logintime']
			for (key,values) in zip(l,loginfo):
				session[key]=values
			#print('验证成功')
			#print(loginfo)
			if session['auth']>2:
				return render_template('home.html',**session)
			else:
				return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),**session)
		else:
			return loginfo[0]
#登出
@app.route('/logout')
def logout():
	useraction.delonline(session['loginname'])
	return render_template('index.html')

#管理主页
#管理员功能
@app.route('/adduser',methods=['get','post'])
def adduser():
	l=[]
	l.append(request.form['loginname'])
	l.append(request.form['passwd'])
	l.append(request.form['endtime'])
	l.append(session['auth']+1)
	l.append(session['loginname'])
	l.append(request.form['contact'])
	
	t=useraction.adduser(*l)
	if t:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),info='增加成功')
	else:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),info='增加失败')
@app.route('/updateuser',methods=['get','post'])
def updateuser():
	l=[]
	l.append(request.form['loginname'])
	l.append(request.form['passwd'])
	l.append(request.form['endtime'])
	l.append(session['auth'])
	l.append(session['creator'])
	l.append(request.form['contact'])
	t=useraction.updateuser(*l)
	if t:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),info='修改成功')
	else:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),info='修改失败')
@app.route('/deluser',methods=['get','post'])
def deluser():
	l=[]
	l.append(request.form['delloginname'])
	l.append(session['loginname'])
	#print(session)
	t=useraction.deluser(*l)
	if t:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),info='删除成功')
	else:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),info='删除失败')
#用户主页
#用户页功能
@app.route('/queryQQ',methods=['get','post'])
def queryQQ():
	
	try:
		thenum=request.args['thenum']	
	except Exception as e:
		#print(e)
		thenum=request.form['thenum']
	
	queryresult=sql.queryqqnum(thenum)
	
	#print(queryresult)
	return render_template('home.html',qqinfo=queryresult,**session)
@app.route('/queryQun',methods=['get','post'])
def queryQun():
	
	try:
		thenum=request.args['thenum']
		
	except Exception as e:
		#print(e)
		thenum=request.form['thenum']
	#print(thenum)
	queryresult=sql.queryqunnum(thenum)
	return render_template('home.html',quninfo=queryresult,**session)
#用户信息页
@app.route('/userpage',methods=['get','post'])
def userpage():
	return render_template('userpage.html')
@app.route('/usersetting',methods=['get','post'])
def usersetting():
	l=[]
	l.append(session['loginname'])
	l.append(request.form['passwd'])
	l.append(session['endtime'])
	l.append(session['auth'])
	l.append(session['creator'])
	l.append(request.form['contact'])
	useraction.updateuser(*l)
	if session['auth']>2:
		return render_template('home.html',**session)
	else:
		return render_template('admin.html',userlist=useraction.getuserlist(session['loginname'],session['creator']),**session)
#一些工具
#网页数据获取
def getpagedata(*namelist):
	d={}
	try:
		for name in namelist:
			d[name]=request.form[name]
	except Exception:
		for name in namelist:
			d[name]=request.args[name]
	return d
#脚本测试
if __name__=='__main__':
	app.debug=True
	app.run(host='0.0.0.0',port=10000,threaded=True)
