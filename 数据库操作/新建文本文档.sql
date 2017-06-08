create database manager;
create table userlist(
						id int not null primary key identity(1,1),
						loginname varchar(20) not null unique,
						passwd varchar(20) not null,
						endtime date not null,
						auth int not null,
						creator varchar(20) not null,
						contact varchar(100));
insert into manager.dbo.userlist values('admin',123456,'2099-12-31',1,'admin','qq:3229582578');
create table onlinelist(
						loginname varchar(20) not null unique,
						logintime float not null,
				
);