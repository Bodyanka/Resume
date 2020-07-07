import psycopg2
import Alpha.error_functions as fc

conn = psycopg2.connect(database="Alpha", user="postgres", password="pass", host="localhost", port=5432)


def create():
    with conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "CREATE TABLE MAIN ("
                    "id SERIAL PRIMARY KEY, "
                    "Symbol_id BIGINT REFERENCES symbols(pair_id) NOT NULL,"
                    "Date_id BIGINT REFERENCES dates(date_id) not NULL,"
                    "a_open TEXT, "
                    "b_open TEXT, "
                    "a_high TEXT, "
                    "b_high TEXT, "
                    "a_low TEXT, "
                    "b_low TEXT, "
                    "a_close TEXT, "
                    "b_close TEXT, "
                    "volume TEXT, "
                    "market_cap TEXT, "
                    "open TEXT, "
                    "high TEXT, "
                    "low TEXT, "
                    "close TEXT, "
                    "SMA TEXT)"
                )

                print('\nMAIN DB created')

            except Exception as e:
                print('\nMAIN DB exists')
                fc.cr_ex_err()
                fc.ex_err()
                print(e)
