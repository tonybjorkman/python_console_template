from sqlalchemy.orm import sessionmaker
import sys
import os
from util.logger import logger
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print(sys.path)
from db import Cat,session

#engine = create_engine('postgresql+psycopg2://postgres:$öfp5wuf33<\
#@localhost/standard_db')
#engine = create_engine('sqlite:///minimal-sql3.db')
# Creates the database schema in case its missing
#Base.metadata.create_all(engine)
#Base.metadata.bind = engine

# create a session with which to interact with the db
#db = sessionmaker(bind=engine)
#session = db()
def run():
    # adds example cat to db
    logger.info('creating cat')
    cat_one = Cat(name="bad cat")
    session.add(cat_one)
    session.commit()

    print("cats in db:"+str(session.query(Cat).all()))

def mytest():
    return True