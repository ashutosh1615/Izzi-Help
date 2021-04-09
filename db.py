#importing
import psycopg2
from config import config

class db:
    def __init__(self,conn,cur):
        self.conn=conn
        self.cur=cur

#connecting to the database

def connect():
    try:
        #read connection parameters
        params=config()
        #connecting to postgresql server
        print('connecting to the postgresql database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        r = db(conn,cur)
        return r
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def cursor_close(cur):
    cur.close()    

               



