import psycopg2 

#connect to the database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

cur = conn.cursor()


#create table with same headers as csv file
cur.execute("""DROP TABLE IF EXISTS phonebook;
CREATE TABLE IF NOT EXISTS phoneBook (
            id INT PRIMARY KEY,
            first_name VARCHAR(255),
            phone_number VARCHAR(255)
            );
        """)

#copy file into the table just created 
with open(r'C:\Users\Lenovo\Desktop\pp2\pp2_new\lab10\phonebook\data.csv', 'r') as f:
    next(f) # Skip the header row.
    #f , <database name>, Comma-Seperated
    cur.copy_from(f, 'phonebook', sep=',')
    #Commit Changes
    conn.commit()
    #Close connection
    conn.close()


f.close()