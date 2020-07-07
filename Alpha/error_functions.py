import time
import psycopg2

conn = psycopg2.connect(database="Alpha", user="postgres", password="pass", host="localhost", port=5432)


def cr_ex_err():
    with conn:
        with conn.cursor() as cur:
            try:
                cur.execute("CREATE TABLE warnings (id SERIAL PRIMARY KEY, Type TEXT, Description TEXT, Time TEXT)")
                print('Warning table created')
            except Exception as e:
                print('Warning table exists', e)


def ex_err():
    tm = time.asctime()
    with conn:
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO warnings (Type, Description, Time) VALUES (%s, %s, %s)",
                            ('Warning', 'No need to create a new table', tm))
                print('Warning inserted\n')
            except Exception as e:
                print('Warning\n', e)
