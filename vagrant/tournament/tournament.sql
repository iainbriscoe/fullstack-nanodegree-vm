-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--drop the table if its there, so that you can start with fresh data 
DROP TABLE IF EXISTS players, matches;

-- create a players table with autoincrementing id, player name, and wins and matches with both default at 0 
CREATE TABLE players ( 	id SERIAL PRIMARY KEY,
						player TEXT, 
						wins int default 0,
						matches int default 0); 
--create a matches table that includes the winner and loser
CREATE TABLE matches ( winner TEXT,
						loser TEXT );
