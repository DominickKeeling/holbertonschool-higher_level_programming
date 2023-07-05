#!/usr/bin/python3
"""Defines State class using SQLAlchemy ORM for a MySQL database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the states table.

    Attributes:
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
