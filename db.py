from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

# TODO: FIgure out why environment variable isn't working
engine = create_async_engine(
    # url = os.getenv("DATABASE_URL"),
    "postgresql+asyncpg://postgres:password@localhost/notes_api",
    echo = True 
)

class Base(DeclarativeBase):
    pass