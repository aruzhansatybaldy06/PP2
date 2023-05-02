import psycopg2 
from config import config
connection=None
try:
    parametres=config()
    connection=psycopg2.connect(**parametres)
    cursor=connection.cursor()
    cursor.close()
except(Exception,psycopg2.DatabaseError) as error:
    print(error)
finally:
    if connection is not None:
        print("Connection")
        connection.close()