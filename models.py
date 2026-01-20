from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
import datetime

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String)
    interaction_type = Column(String)
    summary = Column(Text)
    sentiment = Column(String)
    follow_up = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
