import psycopg2

name = input("FIRST NAME: ")
number = input("PHONE NUMBER: ")

def procedure(first_name, phone_number):
    """Create procedure to insert new user by name and phone, update phone if user already exists"""
    sql = """ INSERT INTO phonebook2 (first_name, phone_number) VALUES(%s, %s) 
        ON CONFLICT (first_name) DO UPDATE
        SET phone_number = EXCLUDED.phone_number || ''; """
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        cur.execute(sql, (first_name, phone_number))

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    procedure(name, number)