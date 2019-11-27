from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///minimal-sql3.db')
# Creates the database schema in case its missing
Base.metadata.create_all(engine)
Base.metadata.bind = engine

# create a session with which to interact with the db
db = sessionmaker(bind=engine)
session = db()

# adds example cat to db
cat_one = Cat(name="good cat")
session.add(cat_one)
session.commit()

print("cats in db:"+str(session.query(Cat).all()))