from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from db.models import Base
from app.settings import config

conn_str = config.get('database', 'conn_string')
engine = create_engine(conn_str)

# Creates the database schema in case its missing
Base.metadata.create_all(engine)
Base.metadata.bind = engine

Session = scoped_session(sessionmaker(bind=engine))
session = Session()