from sqlalchemy import (
    Column,
    Integer
    )

from ..models import Base,DBSession

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
        