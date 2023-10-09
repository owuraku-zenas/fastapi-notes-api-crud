from sqlalchemy import Column, String, Text, DateTime, func
from db import Base
from datetime import datetime

class Note(Base):
    __tablename__ = "notes"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    date_created = Column(DateTime, default=func.now())

    def __repr__(self) -> str:
        return f"<Note {self.title} at {self.date_created}>"
