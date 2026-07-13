from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import URL

# Postgres DB
postgres_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Keshav@123",
    host="localhost",
    database="gsbcommunity"
)

engine = create_engine(postgres_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()