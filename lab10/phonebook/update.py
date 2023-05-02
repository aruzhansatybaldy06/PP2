import psycopg2

# changing phone number by id
def update_phonebook(phone_number, id):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE phonebook
                SET phone_number = %s
                WHERE id = %s"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        # execute the UPDATE  statement
        cur.execute(sql, (phone_number, id))

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
    # Update 
    update_phonebook('+75854785601', 5)