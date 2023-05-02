import psycopg2


def procedure():
    """Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. 
    Check correctness of phone in procedure and return all incorrect data. """
    sql = """INSERT INTO phonebook2 (first_name, phone_number)
    VALUES
    ('Saira', '+77012995005'),
    ('Sabrina', '77012995500'),
    ('Armin', '77012995002'),
    ('Dazai', '+77012995507')
    RETURNING phone_number NOT LIKE '7%';
 """
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        # execute the INSERT statement
        cur.execute(sql)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

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
    procedure()