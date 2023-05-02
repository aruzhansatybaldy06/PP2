import psycopg2


def create_table():
    """Create a new table phonebook2"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS phoneBook2 (
            first_name VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(255)
            
            );
        """)

        cur.execute("""INSERT INTO phonebook2 (first_name, phone_number) VALUES
        ('Aruzhan', '+7475637618'),
        ('Firuza', '+77084236848'),
        ('Aknur', '+77082995408'),
        ('Aina', '+77012995408'),
        ('Bob', '+77012995400'),
        ('Carl', '+77472990000'),
        ('Mike', '+77012900000'),
        ('DiCaprio', '+77012000000'),
        ('James', '+75005412698');
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
    create_table()