from sqlalchemy import (
    Column,
    Integer
    )

from ..models import Base,DBSession

from sqlalchemy.types import String
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship


class Tag(Base):
    
    __tablename__ = 'tags'
    id = Column(Integer,primary_key=True)
    
    name = Column(String(256))
    image = Column(String(2048))
    
    def __init__(self,name,image):
        
        self.name = name
        self.image = image
        
class Badge(Base):
    
    __tablename__ = 'badges'
    id = Column(Integer,primary_key=True)
    
    name = Column(String(256))
    image = Column(String(2048))
    
    def __init__(self,name,image):
        
        self.name = name
        self.image = image
        
class Topic(Base):
    
    __tablename__ = 'topics'
    id = Column(Integer,primary_key=True)
    
    name = Column(String(256))
    description = Column(String(2048))
    image = Column(String(2048))
    
    def __init__(self,name,image,description):
        
        self.name = name
        self.image = image
        self.description = description
        
        