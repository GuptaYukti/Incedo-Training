from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'  # name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # primary key column
    name = Column(String(50), nullable=False)  # name column, cannot be null
    email = Column(String(100), unique=True, nullable=False)  # email column, must be unique and indexed

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
    