from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:catIsTheBest#0526@127.0.0.1:3306/demo"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf8', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()