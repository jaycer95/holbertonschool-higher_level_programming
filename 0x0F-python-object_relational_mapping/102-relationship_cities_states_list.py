#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by(State.id).all()
    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(c.id, c.name, s.name))
    session.close()
