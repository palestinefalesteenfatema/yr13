import sqlite3


conn = sqlite3.connect("user_db.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    name TEXT NOT NULL, 
    email TEXT NOT NULL
)""")

cursor.execute("""
INSERT INTRO users (username,password,name,email) VALUES 
('user1', 'lollll','fatema hamza','22304@students.mrgs.school.nz')
""")

conn.commit()
conn.close()