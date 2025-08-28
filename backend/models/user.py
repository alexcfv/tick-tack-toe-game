from sqlalchemy import Column, Text, Integer
from models.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, nullable=True, primary_key=True)
    user_name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    
    def to_json(self):
        return {
            "user_name" : self.user_name,
            "password" : self.password,
            "id" : self.id
        }