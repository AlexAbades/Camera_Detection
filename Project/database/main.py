# Script to connect to a database 

import psycopg2 
from config import config

def connect():
    connection = None
    try:
        params = config()
        print("Connecting to the postgreSQL database ...")
        connection = psycopg2.connect(**params)
        # Create a cursor object -> Capable to send commands to the SQL 
        # All commands will be executed through the cursor object
        crsr = connection.cursor()
        print("PostgreSQL database version: ")
        crsr.execute("SELECT version()")
        # Read the results set 
        db_version = crsr.fetchone()
        print(db_version)
        # Close the cursor
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection:
            connection.close()
            print("Database connection terminated.")
        

if __name__ == "__main__":
    connect()