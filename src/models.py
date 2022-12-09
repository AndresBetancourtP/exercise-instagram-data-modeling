import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    created_at = Column(String(250))
    updated_at = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    comment = Column(String(250))
    created_at = Column(String(250))
    updated_at = Column(String(250))
    total_likes = Column(Integer)

class PostComment(Base):
    __tablename__ = 'postComment'
    comment_id = Column(Integer, primary_key=True)
    author_comment_id = Column(Integer, ForeignKey('user.user_id'))
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.post_id'))
    

class Likes(Base):
    __tablename__ = 'likes'
    like_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    user_likeit_id = Column(Integer, ForeignKey('user.user_id'))
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')