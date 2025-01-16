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
    commits = relationship("Commit", back_populates="repository")

class Commit(Base):
    __tablename__ = "commits"
    
    id = Column(Integer, primary_key=True, index=True)
    repository_id = Column(Integer, ForeignKey("repositories.id"))
    hash = Column(String, index=True)
    author = Column(String)
    date = Column(DateTime)
    message = Column(Text)
    files_changed = Column(Integer)
    insertions = Column(Integer)
    deletions = Column(Integer)
    repository = relationship("Repository", back_populates="commits")

def get_db_url():
    # 检查是否在 Vercel 环境中运行
    if os.environ.get('VERCEL_ENV'):
        return 'sqlite:///:memory:'
    else:
        # 本地开发环境使用文件数据库
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gitscan.db')
        return f'sqlite:///{db_path}'

def init_db():
    engine = create_engine(get_db_url())
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return engine, SessionLocal
