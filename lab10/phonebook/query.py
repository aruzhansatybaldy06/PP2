import psycopg2


def get_phonebook():
    """ query data from the phonebook table """
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        cur.execute("SELECT id, first_name FROM phonebook ORDER BY first_name")
        print("The number of parts: ", cur.rowcount)
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
   get_phonebook()