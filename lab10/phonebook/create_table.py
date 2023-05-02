import psycopg2


def create_phonebook():
    """ create a table"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        #create a table
        cur.execute("""CREATE TABLE IF NOT EXISTS phoneBook (
            id INT PRIMARY KEY,
            first_name VARCHAR(255),
            phone_number VARCHAR(255)
            );
        """)

        # insert some values
        cur.execute("""INSERT INTO phonebook (id, first_name, phone_number) VALUES
        (1, 'Aknur', '+77475637615'),
        (2, 'Firuza', '+77084236847'),
        (3, 'Aruzhan', '+77082995405'),
        (4, 'Aina', '+77012995405'),
        (5, 'Saira', '+77012995005'),
        (6, 'Sabrina', '+77012995500'),
        (7, 'Mike', '+77012995852'),
        (8, 'Dad', '+77012998000'),
        (9, 'James', '+75005412698');
        """)

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
    create_phonebook()