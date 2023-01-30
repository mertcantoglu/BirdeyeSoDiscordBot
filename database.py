import sqlite3
from logger import Logger

class Database:
    def __init__(self,db_file) -> None:
        self.logger = Logger()
        self.file = db_file
    
    def saveHash(self,_hash):
        try:
            conn = sqlite3.connect(self.file)
            cursor = conn.cursor()
            sql = """CREATE TABLE IF NOT EXISTS HASH(
            id integer primary key AUTOINCREMENT,
            hash TEXT)"""
            cursor.execute(sql)
            cursor.execute("""SELECT hash
                   FROM HASH
                   WHERE hash=?""",
                (_hash,))
            result = cursor.fetchone()  
            if result:
                return False
            else:
                cursor.execute("INSERT INTO HASH (hash)Values(?)",(_hash,))
                conn.commit()
                conn.close()
                print(f"Txn Hash saved to DB {_hash}")
                return True
        except:
            self.logger.printe("Database error!")

    def getLastHash(self):
        try:
            conn = sqlite3.connect(self.file)
            cursor = conn.cursor()
            sql = """CREATE TABLE IF NOT EXISTS HASH(
            id integer primary key AUTOINCREMENT,
            hash TEXT)"""
            cursor.execute(sql)
            cursor.execute("SELECT * FROM HASH ORDER BY id DESC LIMIT 1")
            result = cursor.fetchone()  
            conn.close()
        except:
            self.logger.printe("Database error!")
        try:
            return (result[1])
        except:
            return ""
        
    def hashExists(self,_hash):
        conn = sqlite3.connect(self.file)
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS HASH(
        id integer primary key AUTOINCREMENT,
        hash TEXT)"""
        cursor.execute(sql)
        cursor.execute("""SELECT hash
                   FROM HASH
                   WHERE hash=?""",
                (_hash,))

        result = cursor.fetchone()  