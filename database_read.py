
from database_definitions import Player, Team, Base
from sqlalchemy import create_engine
engine = create_engine('sqlite:///die_stats.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
# Return the first Person from all Persons in the database
person = session.query(Player).first()

print(person.name)