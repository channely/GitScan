from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os

Base = declarative_base()

class Repository(Base):
    __tablename__ = "repositories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    path = Column(String)
    url = Column(String, nullable=True)  
    last_updated = Column(DateTime, default=datetime.utcnow)
    last_analyzed = Column(DateTime)  
    commits = relationship("Commit", back_populates="repository", cascade="all, delete-orphan")

class Commit(Base):
    __tablename__ = "commits"
    
    id = Column(Integer, primary_key=True, index=True)
    repository_id = Column(Integer, ForeignKey("repositories.id", ondelete="CASCADE"))
    hash = Column(String, index=True)
    author = Column(String)
    date = Column(DateTime)
    message = Column(Text)
    files_changed = Column(Integer)
    insertions = Column(Integer)
    deletions = Column(Integer)
    repository = relationship("Repository", back_populates="commits")

def get_db_url():
    # 默认使用本地文件数据库
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gitscan.db')
    db_url = f'sqlite:///{db_path}'
    
    # 仅在 Vercel 环境中使用内存数据库
    if os.environ.get('VERCEL_ENV') == 'production':
        db_url = 'sqlite:///:memory:'
    
    return db_url

def init_db():
    # 创建数据库引擎
    engine = create_engine(
        get_db_url(),
        connect_args={'check_same_thread': False}  # 允许多线程访问
    )
    
    # 创建会话工厂
    SessionLocal = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
    
    # 确保所有表都已创建
    Base.metadata.create_all(engine)
    
    return engine, SessionLocal
