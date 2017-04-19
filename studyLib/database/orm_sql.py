#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from sqlalchemy import Column, String, create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

'''Object-Relational Mapping'''

__author__ = 'Mr.Huo'

# 创建对象的基类
Base = declarative_base()


class User(Base):
    """创建数据库表对应的类"""
    # 表名
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    #一对多
    books =relationship('Book')

class Book(Base):
    """创建数据库表对应的类"""
    # 表名
    __tablename__ = 'book'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 多对一，通过外键关联到user表
    user_id = Column(String(20),ForeignKey('user.id'))

class School(Base):
    """创建数据库表对应的类"""
    # 表名
    __tablename__ = 'school'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


def main():
    # 初始化数据库连接：数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
    DB_CONNECT_STRING = 'mysql+mysqlconnector://root:zhixuan_860606@localhost:3306'
    user_engine = create_engine(DB_CONNECT_STRING, echo=False)
    # 创建DBsession类型
    DBsession = sessionmaker(bind=user_engine)
    # 创建DBsession对象
    session = DBsession()
    # 创建一个数据库
    try:
        session.execute('CREATE database test')
    except Exception as err:
        print(err)
    # 选择一个数据库
    session.execute('USE test')
    # 创建要使用的表
    session.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
    session.execute('CREATE TABLE school (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
    # 添加数据
    new_user = User(id='1', name='haha1')
    session.add(new_user)
    new_user = User(id='2', name='haha2')
    session.add(new_user)
    new_school = School(id='1', name='haha-hahh1')
    session.add(new_school)
    new_school = School(id='2', name='haha-hahh2')
    session.add(new_school)
    #new_book = Book(id='1', name='haha-book-1',user_id = '1')
    #session.add(new_book)
    session.commit()

    # 查询数据
    user_result1 = session.query(User)
    print('type:', type(user_result1))
    print('id1:', user_result1)
    print('id2:', user_result1.statement)
    print('id3:', user_result1.all())
    for user in user_result1:
        print(type(user), id(user))
        print(user.id, user.name)
    print('按ID过滤   id=1 name=%s' % user_result1.filter(User.id == '1').first().name)
    print('按主键过滤 id=2 name=%s' % user_result1.get('2').name)
    #
    user_result2 = session.query(User.id)
    print('type:',type(user_result2))
    print('all:',user_result2.all())
    # 删除创建的数据库
    session.execute('drop database test')
    session.close()


if __name__ == '__main__':
    main()
