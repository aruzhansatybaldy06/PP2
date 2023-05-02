import psycopg2

id = int(input("ID: "))
name = input("FIRST NAME: ")
number = input("PHONE NUMBER: ")

try:
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)
    cur = conn.cursor()

    cur.execute("""
    DROP TABLE IF EXISTS phonebook;
    CREATE TABLE IF NOT EXISTS phonebook (
            id INT PRIMARY KEY,
            first_name VARCHAR(255),
            phone_number VARCHAR(255)
            );
        """)
    
    cur.execute("""INSERT INTO phonebook (id, first_name, phone_number) VALUES
        (%s, %s, %s);
        """, (id, name, number))
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    conn.close()