#!/usr/bin/python3
"""Script that updates the name of the State object where id = 2
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).get(2)
    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()
    session.close()
