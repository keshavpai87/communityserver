from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.engine import URL

# Postgres DB
postgres_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="Keshav@123",
    host="localhost",
    database="telusko"
)

# MySql DB
mysql_url = URL.create(
    drivername="mysql+pymysql",
    username="user",
    password="my@password",
    host="localhost",
    port=3306,
    database="testdb"
)

# db_url = "dbtype://username:password@localhost:portnumber/dbname"
password = "my@password"
encoded_password = quote_plus(password)
# db_url = "postgresql+psycopg2://postgres:{encoded_password}@localhost/telusko"
engine = create_engine(postgres_url)
session = sessionmaker(autoflush = False, bind = engine, autocommit = False)