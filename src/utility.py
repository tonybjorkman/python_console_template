from db import *

def load_test_data():
    # Create a new cat
    cat = Cat(name='Fluffy', age=5)
    # Add it to the session
    session.add(cat)
    # Commit the change
    session.commit()
    # Print out the cat
    print(cat)

def create_db():
    Base.metadata.create_all(bind=engine)
    load_test_data()


if __name__ == '__main__':
    create_db()