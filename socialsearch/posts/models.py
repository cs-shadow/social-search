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
        
    