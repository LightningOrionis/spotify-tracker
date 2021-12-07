from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
