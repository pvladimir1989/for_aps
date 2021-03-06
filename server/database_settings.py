import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

SERVER_POSTGRES_CONNECTION = os.getenv("SERVER_POSTGRES_CONNECTION", None)
engine = create_engine(SERVER_POSTGRES_CONNECTION, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
