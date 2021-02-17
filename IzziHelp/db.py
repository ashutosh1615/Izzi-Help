#importing
import psycopg2
from config import config
#connecting to the database

def connect(cur):
    try:
        #read connection parameters
        params=config()
        #connecting to postgresql server
        print('connecting to the postgresql database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        return cur
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def cursor_close(cur):
    cur.close()    

               



