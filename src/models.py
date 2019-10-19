from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Cloumn,String,Integer,Text,DataTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://szx:123@localhost:3306/work")
Base = declearative_base(bind=engine)
Session = sessionmaker(bind=engine)


Class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key='True')
    nickname = Column(String(10),unique='True')
    password = Column(string(128))
    gender = Column(String(10))
    city = Column(String(10))
    bio = Column(String(256))

Class Weibo(Base):
    __tablename__ = 'weibo'
    id = Column(Integer,primary_key='True')
    user_id = Column(Integer)
    content = Column(Text)
    created = Column(DataTime)

Class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer,primary_key='True')
    use_id = Column(Integer)
    wb_id = Column(Integer)
    cmt_id = Column(Integer,default=0)
    content = Column(Text)
    created = Column(DataTime)

    @property
    def up_comment(self):
        session = Session()
        return session.query(Comment).get(self.cmt_id)


