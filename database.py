from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:Root%40123@localhost:3306/ecommerce"
DATABASE_URL="mysql+pymysql://avnadmin:AVNS_7pyjmqWYY1yrN5A9Qaw@creative-kuchikajhansirani-6090.j.aivencloud.com:27979/defaultdb?ssl-mode=REQUIRED"

engine = create_engine(DATABASE_URL)

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
