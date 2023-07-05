#!/usr/bin/python3
"""Lists all State objects containing letter 'a' from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State)\
                        .order_by(State.id)\
                        .filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

    session.close()
