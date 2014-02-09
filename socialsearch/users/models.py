from sqlalchemy import (
    Column,
    Integer
    )

from ..models import Base,DBSession
from ..tags.models import Badge,Topic

from sqlalchemy.types import String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    
    given_name = Column(String(256))
    formatted = Column(String(256))
    family_name = Column(String(256))
    
    email = Column(String(256),nullable = False)
    
    user_id = Column(String(256))
    domain = Column(String(256))
    access_token = Column(String(256))
    refresh_token = Column(String(256))
    
    profile_pic = Column(String(512))
    
    about = Column(String(512))
    
    password = Column(String(256))
    
    def __init__(self,
                 given_name,formatted,family_name,
                 email,user_id,domain,access_token,refresh_token,
                 about,
                 password,profile_pic):
        
        self.given_name = given_name
        self.formatted = formatted
        self.family_name = family_name
        
        self.email = email
        self.user_id = user_id
        self.domain = domain
        self.access_token = access_token
        self.refresh_token = refresh_token
        
        self.password = password
        
        self.about = about
        self.profile_pic = profile_pic
        
        
class UserStats(Base):
    
    __tablename__ = 'user_stats'
    id = Column(Integer,primary_key=True)
    
    user_id = Column(Integer,ForeignKey('users.id'),default = 1)
    user = relationship("User",foreign_keys=[user_id])
    
    points = Column(Integer)
    
    def __init__(self,user_id,points):
        
        self.user_id = user_id
        self.points = points
        
class UserBadge(Base):
    
    __tablename__ = 'user_badges'
    id = Column(Integer,primary_key=True)
    
    user_id = Column(Integer,ForeignKey('users.id'),default = 1)
    user = relationship("User",foreign_keys=[user_id])
    
    badge_id = Column(Integer,ForeignKey('badges.id'),default = 1)
    badge = relationship("Badge",foreign_keys=[badge_id])
    
    def __init__(self,badge_id,user_id):
        
        self.user_id = user_id
        self.badge_id = badge_id
        
        
class UserFollowedTopic(Base):
    
    __tablename__ = 'user_followed_topics'
    id = Column(Integer,primary_key=True)
    
    user_id = Column(Integer,ForeignKey('users.id'),default = 1)
#     user = relationship("User",foreign_keys=[user_id])
    
    topic_id = Column(Integer,ForeignKey('topics.id'),default = 1)
#     topic = relationship("Topic",foreign_keys=[topic_id])
    
    def __init__(self,topic_id,user_id):
        
        self.user_id = user_id
        self.topic_id = topic_id
        
        