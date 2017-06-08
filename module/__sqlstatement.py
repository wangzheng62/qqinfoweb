#userlist操作
USERLIST={'检查用户名':'select loginname from manager.dbo.userlist where loginname=\'%s\';','获取用户信息':'select * from manager.dbo.userlist where loginname=\'%s\' and passwd=\'%s\';'}
#onlinelist操作
ONLINELIST={'检查登录信息':'select loginname,logintime from manager.dbo.onlinelist where loginname=\'%s\';','插入登录信息':'insert into manager.dbo.onlinelist values (\'%s\',%s);','删除登录信息':'delete from manager.dbo.onlinelist where loginname=\'%s\';'}