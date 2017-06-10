import datetime
import inspect

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_definitions import Player, Base, Team, PlayerGame, PlayerStats, \
    TeamStats


engine = create_engine('sqlite:///die_stats.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

def new_user(name, age = None, wingspan = None, hand = None):
    id = session.query(Player).count()
    new_person = Player(player_id = id, name = name, age = age, wingspan = wingspan, hand = hand)
    new_playerstats = PlayerStats(player_id = id, year = datetime.datetime.now().year)
    session.add(new_person)
    session.add(new_playerstats)
    
def new_team(team_name, player1_id, player2_id):
    id = session.query(Team).count()
    new_team = Team(team_id = id, team_name = team_name, player1 = player1_id, player2 = player2_id)
    new_teamstats = TeamStats(team_id = id, year = datetime.datetime.now().year)
    session.add(new_team)
    
def new_game(game_list):
    for player in game_list:
        print(player)
        stat_list = string_breaker(player)
        new_game = PlayerGame(player_id = stat_list.get("player_id"), game_id = stat_list.get("game_id"), 
                              total_throws = stat_list.get("total_throws"), points = stat_list.get("total_points"), 
                              hits = stat_list.get("hits"), tinks = stat_list.get("tinks"), 
                              sinks = stat_list.get("sinks"), dicks = stat_list.get("dicks"),
                              shorts = stat_list.get("shorts"), fives = stat_list.get("fives"))
        
        print(new_game)
        print(stat_list)
        player_stats = session.query(PlayerStats)
        ps = player_stats.filter_by(player_id = stat_list.get("player_id")).scalar()
        ps.player_id += stat_list.get("player_id")
        ps.total_throws += stat_list.get("total_throws")
        ps.points += stat_list.get("total_points")
        ps.hits += stat_list.get("hits") 
        ps.tinks += stat_list.get("tinks")
        ps.sinks += stat_list.get("sinks")
        ps.dicks += stat_list.get("dicks")
        ps.shorts += stat_list.get("shorts")
        ps.fives += stat_list.get("fives")
        
        session.add(ps)
        session.add(new_game)


def string_breaker(player_string):
    list = {}
    list["player_id"] = int(player_string[0:3])
    list["game_id"] = int(player_string[3:6])
    list["total_throws"] = int(player_string[6:8])
    list["total_points"] = int(player_string[8:10])
    list["hits"] = int(player_string[10:12])
    list["tinks"] = int(player_string[12:14])
    list["sinks"] = int(player_string[14:16])
    list["dicks"] = int(player_string[16:17])
    list["shorts"] = int(player_string[18:20])
    list["fives"] = int(player_string[20:22])
    return list
def main():
    new_user("Alex Goodell")
    new_game(["0000013005000101002805"])
    session.commit()
    
if __name__ == "__main__":
    main()