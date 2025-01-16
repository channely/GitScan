from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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

# 创建数据库引擎和表
engine = create_engine('sqlite:///gitscan.db')
Base.metadata.create_all(engine)
