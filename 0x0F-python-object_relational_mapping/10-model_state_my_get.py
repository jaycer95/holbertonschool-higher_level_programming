#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    if session.query(State).filter(State.name == argv[4]).first():
        print("{}".format(session.query(State).filter(State.name == argv[4])
                          .first().id))
    else:
        print("Not found")
    session.close()
