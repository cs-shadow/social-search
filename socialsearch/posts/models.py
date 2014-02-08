from sqlalchemy import (
    Column,
    Integer
    )

from ..models import Base,DBSession

from sqlalchemy.types import String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

from ..util import getTimeEpoch

from ..users.models import User
from ..tags.models import Tag,Badge

class Post(Base):
    
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True)
    
    user_id = Column(Integer,ForeignKey('users.id'),default = 1)
    user = relationship("User",foreign_keys=[user_id])
    
    time = Column(Integer)
    rank_weight = Column(Integer)
    
    content = Column(String(2048))
    content_type = Column(String(256))
    
    def __init__(self,user_id,rank_weight,
                    content,content_type):
        
        self.user_id = user_id
        self.rank_weight = rank_weight
        
        self.content = content
        self.content_type = content_type
        
        self.time = getTimeEpoch()
        
class PostTag(Base):
    
    __tablename__ = 'post_tags'
    id = Column(Integer,primary_key=True)
    
    post_id = Column(Integer,ForeignKey('posts.id'),default = 1)
    post = relationship("Post",foreign_keys=[post_id])
    
    tag_id = Column(Integer,ForeignKey('tags.id'),default = 1)
    tag = relationship("Tag",foreign_keys=[tag_id])
    
    def __init__(self,post_id,tag_id):
        
        self.post_id = post_id
        self.tag_id = tag_id
        
class PostLike(Base):
    
    __tablename__ = 'post_likes'
    id = Column(Integer,primary_key=True)
    
    post_id = Column(Integer,ForeignKey('posts.id'),default = 1)
    #Post Relation If Required
    
    user_id = Column(Integer,ForeignKey('users.id'),default = 1)
    #User Relation If Required
    
    def __init__(self,post_id,user_id):
        
        self.post_id = post_id
        self.user_id = user_id
        

class PostDislike(Base):
    
    __tablename__ = 'post_dislikes'
    id = Column(Integer,primary_key=True)
    
    post_id = Column(Integer,ForeignKey('posts.id'),default = 1)
    #Post Relation If Required
    
    user_id = Column(Integer,ForeignKey('users.id'),default = 1)
    #User Relation If Required
    
    def __init__(self,post_id,user_id):
        
        self.post_id = post_id
        self.user_id = user_id
        
        