#
# Database access functions for the web forum.
# 

import psycopg2
import bleach


## Get posts from database.
def GetAllPosts():
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("UPDATE posts SET content='cheese' where content like '%script%'")
    c.execute("DELETE FROM posts where content like '%cheese%'")
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    
    posts = ({'content': str(row[1]), 'time': str(row[0])}
             for row in c.fetchall())
    
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    c.execute("INSERT INTO posts (content) VALUES (%s)",
              (bleach.clean(content),))
    
    DB.commit()
    DB.close()
