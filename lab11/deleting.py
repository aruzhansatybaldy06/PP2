import psycopg2


def delete_part(first_name):
    """Implement procedure to deleting data from tables by username or phone"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        # execute the DELETE statement
        cur.execute("DELETE FROM phonebook2 WHERE first_name = %s", (first_name,))
        # deleting by phone number
        # cur.execute("DELETE FROM phonebook2 WHERE phone_number = %s", (phone_number,))

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
    deleted_rows = delete_part('Firuza')
    