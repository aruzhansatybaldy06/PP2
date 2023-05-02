import psycopg2



def create_table():
    """ create tables in the PostgreSQL database"""
    sql = ("""CREATE TABLE IF NOT EXISTS snake (
            username VARCHAR(255),
            score INT
            );
        """)
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()
        cur.execute(sql)
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