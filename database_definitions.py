import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Game(Base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key = True)
    team1 = Column(Integer, ForeignKey('Teams.team_id'))
    team2 = Column(Integer, ForeignKey('Teams.team_id'))
    date = Column(String(250))
    total_throws = Column(Integer, default = 0)
    total_points = Column(Integer, default = 0)
    total_hits = Column(Integer, default = 0)
    total_tinks = Column(Integer, default = 0)
    total_sinks = Column(Integer, default = 0)
    total_dicks = Column(Integer, default = 0)
    total_shorts = Column(Integer, default = 0)
    total_fives = Column(Integer, default = 0)
 
class Player(Base):
    __tablename__ = 'Players'
    #This taable represents a die player, with various stats such as age, wingspan, and handedness
    player_id = Column(Integer, primary_key=True)
    name = Column(String(250))
    age = Column(Integer)
    wingspan = Column(Integer)
    hand = Column(String(250))
    
    
 
class Team(Base):
    __tablename__ = 'Teams'
    #this table represents teams, with two players
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(250))
    player1 = Column(Integer, ForeignKey('Players.player_id'))
    player2 = Column(Integer, ForeignKey('Players.player_id'))
    
class PlayerStats(Base):
    __tablename__ = "PlayerStats"
    #this  table represents an individual player's accumulative stats
    player_id = Column(Integer, ForeignKey('Players.player_id'), primary_key = True)
    year = Column(Integer)
    total_throws = Column(Integer, default = 0)
    points = Column(Integer, default = 0)
    hits = Column(Integer, default = 0)
    tinks = Column(Integer, default = 0)
    sinks = Column(Integer, default = 0)
    dicks = Column(Integer, default = 0)
    shorts = Column(Integer, default = 0)
    fives = Column(Integer, default = 0)
    
    
class TeamStats(Base):
    __tablename__ = "TeamStats"
    team_id = Column(Integer, ForeignKey('Teams.team_id'), primary_key = True)
    year = Column(Integer)
    total_throws = Column(Integer, default = 0)
    points = Column(Integer, default = 0)
    hits = Column(Integer, default = 0)
    tinks = Column(Integer, default = 0)
    sinks = Column(Integer, default = 0)
    dicks = Column(Integer, default = 0)
    shorts = Column(Integer, default = 0)
    fives = Column(Integer, default = 0)
    
class PlayerGame(Base):
    __tablename__ = 'PlayerGames'
    player_id = Column(Integer, primary_key = True)
    game_id = Column(Integer, ForeignKey('Games.id'))
    total_throws = Column(Integer, default = 0)
    points = Column(Integer, default = 0)
    hits = Column(Integer, default = 0)
    tinks = Column(Integer, default = 0)
    sinks = Column(Integer, default = 0)
    dicks = Column(Integer, default = 0)
    shorts = Column(Integer, default = 0)
    fives = Column(Integer, default = 0)
    
    

 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///die_stats.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)