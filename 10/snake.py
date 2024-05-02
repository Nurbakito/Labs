import pygame
from level1 import level1
from level2 import level2
import psycopg2


conn = psycopg2.connect(
    dbname="snake",  
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE
    );
""")


cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        level INTEGER,
        score INTEGER
    );
""")

def get_username():
    username = input("Enter your username: ")
    return username

def get_user_level(username):
    cur.execute("""
        SELECT level FROM user_score 
        JOIN users ON user_score.user_id = users.id 
        WHERE username = %s
        ORDER BY id DESC LIMIT 1;
    """, (username,))
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return 0

def save_score(user_id, level, score):
    cur.execute("""
        INSERT INTO user_score (user_id, level, score)
        VALUES (%s, %s, %s);
    """, (user_id, level, score))
    conn.commit()

def create_user(username):
    cur.execute("""
        INSERT INTO users (username)
        VALUES (%s);
    """, (username,))
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    username = get_username()
    user_id = create_user(username)
    user_level = get_user_level(username)
    
    if user_level > 0:
        print(f"Welcome back, {username}! You are currently on level {user_level}.")
    
  
    score = level1(0)

  
    save_score(user_id, 1, score)

   
    score = level2(score)

   
    save_score(user_id, 2, score)


    cur.close()
    conn.close()
