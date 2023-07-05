#!/usr/bin/python3
"""Prints the State object with the name passed as argument."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
                   .filter(State.name == state_name)\
                   .first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
