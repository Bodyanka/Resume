import psycopg2
import Alpha.get_all as ga

conn = psycopg2.connect(database="Alpha", user="postgres", password="pass", host="localhost", port=5432)


def create_symbols():
    with conn:
        with conn.cursor() as cur:

            try:
                cur.execute(
                    "CREATE TABLE symbols("
                    "pair_id SERIAL PRIMARY KEY, "
                    "pair TEXT UNIQUE not NULL)"
                )

                print('\nsymbols created')

            except Exception as e:
                print('\nsymbols exists')
                print(e)


def insert_symbols(source):
    with conn:
        with conn.cursor() as cur:
            for symb in source:
                try:
                    cur.execute("INSERT INTO symbols (pair) VALUES ('USD_" + symb + "') ON CONFLICT DO NOTHING")
                except Exception as e:
                    print('Error in symbols')
                    print(e)
    print('Symbols inserted')


def insert_sma(source):
    with conn:
        with conn.cursor() as cur:
            for symb in source:
                try:
                    cur.execute("INSERT INTO symbols (pair) VALUES ('" + symb + "') ON CONFLICT DO NOTHING")
                except Exception as e:
                    print('Error in SMA')
                    print(e)
    print('SMA inserted')


def main_symbols():
    pairs_symb = ga.crypto_symbols + ga.curr_symbols
    sma_symb = ga.tech_symbols

    create_symbols()
    insert_symbols(pairs_symb)
    insert_sma(sma_symb)


def create_dates():
    with conn:
        with conn.cursor() as cur:

            try:
                cur.execute(
                    "CREATE TABLE dates("
                    "date_id SERIAL PRIMARY KEY, "
                    "date TEXT UNIQUE not NULL)"
                )

                print('\ndates created')

            except Exception as e:
                print('\ndates exists')
                print(e)


def insert_dates(source):
    with conn:
        with conn.cursor() as cur:
            for symb in source:
                try:
                    cur.execute("INSERT INTO dates (date) VALUES ('" + str(symb) + "') ON CONFLICT DO NOTHING")
                except Exception as e:
                    print('Error in dates')
                    print(e)
    print('Dates inserted')


def get_dates():
    mass = []
    for year in range(2000, 2021):
        for month in range(1, 13):
            for day in range(1, 32):

                if len(str(month)) == 1:
                    mnt = '0' + str(month)
                else:
                    mnt = str(month)

                if len(str(day)) == 1:
                    d = '0' + str(day)
                else:
                    d = str(day)

                mass.append((str(year) + "-" + mnt + "-" + d))
    return mass


def main_dates():
    create_dates()
    insert_dates(get_dates())
