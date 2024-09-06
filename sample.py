import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,  
        password VARCHAR(255) NOT NULL
)
""")

username0, password0 = "admin", hashlib.sha256("admin".encode()).hexdigest()
username1, password1 = "wesem", hashlib.sha256("wesem_mdp".encode()).hexdigest()
username2, password2 = "marc23", hashlib.sha256("marc_mdp".encode()).hexdigest()
username3, password3 = "lucie1970", hashlib.sha256("lucie_mdp".encode()).hexdigest()
username4, password4 = "julien94", hashlib.sha256("julien_mdp".encode()).hexdigest()
username5, password5 = "client", hashlib.sha256("client_mdp".encode()).hexdigest()
username6, password6 = "test", hashlib.sha256("test_mdp".encode()).hexdigest()
username7, password7 = "youcef", hashlib.sha256("youcef_mdp".encode()).hexdigest()
username8, password8 = "12345", hashlib.sha256("12345_mdp".encode()).hexdigest()

cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username0, password0))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username1, password1))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username2, password2))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username3, password3))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username4, password4))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username5, password5))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username6, password6))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username7, password7))
cur.execute("INSERT INTO userdata(username, password) VALUES(?,?)",(username8, password8))

conn.commit()