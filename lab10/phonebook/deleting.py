import psycopg2


def delete_part(first_name):
    """implement deleting data from tables by username of phone"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

         # execute the DELETE statement
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (first_name,))

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
    