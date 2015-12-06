#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    #deletes the contents of table matches
    DB().execute("DELETE FROM matches", True)


def deletePlayers():
    """Remove all the player records from the database."""
    #deletes the contents of table players
    DB().execute("DELETE FROM players", True)


def countPlayers():
    """Returns the number of players currently registered."""
    #gets the player column from the players table
    conn = DB().execute("SELECT COUNT(player) FROM players;")
    #gets the result of the select statement
    count = conn["cursor"].fetchone()[0]
    conn["cursor"].close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    #inserts a new player into the players table, bleach cleans the input to avoid attack 
    c.execute("INSERT INTO players (player) VALUES (%s)", (bleach.clean(name), ))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    #gets id, player, wins and matches ordered by most wins
    conn = DB().execute("select id, player, wins, matches FROM players order by wins desc")
    #conn = DB().execute("SELECT id FROM players UNION SELECT player FROM players UNION SELECT COUNT(winner) as winners FROM matches GROUP BY winner UNION SELECT SUM(COUNT(loser),winners) as losers FROM matches GROUP BY loser")
    #conn = DB().execute("SELECT players.id, players.player, count(matches.winner) AS winners, count(matches.loser) + winners AS total_matches FROM players JOIN matches ON players.player=matches.winner=matches.loser")
    #collects the select rows into a list
    playersList = list(conn["cursor"].fetchall())
    conn["cursor"].close()
    return playersList


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    #updates number of wins and the number of matches played for the winner
    c.execute("UPDATE players SET wins = wins + 1, matches = matches +1 WHERE id = (%s)", (bleach.clean(winner), ))
    #updates the number of matches for the loser
    c.execute("UPDATE players SET matches = matches + 1 WHERE id = (%s)", (bleach.clean(loser), ))
    #add a match to matches table
    c.execute("UPDATE matches SET winner = (%s), loser = (%s)", (bleach.clean(winner), bleach.clean(loser)))
    DB.commit()
    DB.close()




def swissPairings():
    #fetch entire table
    conn = DB().execute("SELECT id, player FROM players ORDER BY wins")
    playersList = list()
    row = conn["cursor"].fetchone()
    while row is not None:
        aTuple = ()
        count = 0
        #build tuples of matches
        while count < 2:
            aTuple = aTuple + row
            row = conn["cursor"].fetchone()
            count = count + 1 
        playersList.append(aTuple)
    conn["cursor"].close()
    return playersList




class DB:
    def __init__(self, connectionString="dbname=tournament"):

        self.conn = psycopg2.connect(connectionString)

    def cursor(self):

        return self.conn.cursor();

    def execute(self, queryString, closeCall=False):

        cursor = self.cursor()
        cursor.execute(queryString)
        if closeCall:
            self.conn.commit()
            self.close()
        return {"connect": self.conn, "cursor": cursor if not closeCall else None}

    def close(self):

        return self.conn.close()
    
