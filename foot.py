import psycopg2
from config import config
# connection = psycopg2.connect(host="localhost", port="5433", database="footballers",
#             user="postgres", password="aditya10")

def connect():
    connection = None
    try: 
        params = config()
        print('Connection to the postgreSQL database...')
        connection = psycopg2.connect(**params)

        crsr = connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')

if __name__ == "__main__":
    connect()