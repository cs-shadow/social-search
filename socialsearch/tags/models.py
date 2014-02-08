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
    
    def __init__(self,name,created_by):
        
        self.name = name
        
class Badge(Base):
    
    __tablename__ = 'badges'
    id = Column(Integer,primary_key=True)
    
    name = Column(String(256))
    
    def __init__(self,name):
        
        self.name = name
        
        