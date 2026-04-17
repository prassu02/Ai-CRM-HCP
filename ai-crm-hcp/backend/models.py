from sqlalchemy import Column, Integer, String, Text
from db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String)
    summary = Column(Text)
    next_action = Column(String)