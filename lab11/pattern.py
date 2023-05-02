import psycopg2

def pattern():
    """ Function that returns all records based on a pattern (example of pattern: part of name, phone number) """
    sql_by_name = """SELECT
	        first_name,
            phone_number
        FROM
	        phonebook2
        WHERE
	        first_name LIKE 'A%';"""
    sql_by_phone = """SELECT
	        first_name,
            phone_number
        FROM
	        phonebook2
        WHERE
	        phone_number LIKE '+7708%';"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        cur.execute(sql_by_phone)
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
   pattern()