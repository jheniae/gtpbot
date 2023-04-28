from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserSettings(Base):
    __tablename__ = "user_settings"
    user_id = Column(Integer, primary_key=True)
    gpt_version = Column(String, nullable=False)

