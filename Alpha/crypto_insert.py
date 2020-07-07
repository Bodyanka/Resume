import os
import sys
import time
import psycopg2
import Alpha.get_all as ga

conn = psycopg2.connect(database="Alpha", user="postgres", password="pass", host="localhost", port=5432)


def crypto_insertion(pair, dmass, csd):
    with conn:
        with conn.cursor() as cur:
            try:
                
                # finding symbol id from existing table with symbols
                cur.execute('SELECT * FROM symbols')
                for row in cur:
                    if row[1] == 'USD_' + str(pair[1]['2. Digital Currency Code']):
                        symb_id = row[0]

                # finding all symbols and dates from main and inserting them to the lists

                cur.execute('Select symbol_id, date_id FROM main')

                for row in cur:
                    if (row[0], row[1]) not in csd:
                        csd.append((row[0], row[1]))

                # running through all dates in json file 
                for date in reversed(pair[0]):

                    # replacing date with date_id
                    for i in dmass:
                        if date == i[1]:
                            date_id = i[0]

                    # insert only if symbol and date in the same time aren`t in table before
                    if (symb_id, date_id) not in csd:
                        cur.execute("INSERT INTO MAIN ("
    
                                    "Symbol_id,"
                                    "Date_id,"
    
                                    "a_open, "
                                    "b_open, "
                                    "a_high, "
                                    "b_high, "
                                    "a_low, "
                                    "b_low, "
                                    "a_close, "
                                    "b_close, "
                                    "volume, "
                                    "market_cap, "
    
                                    "open, "
                                    "high, "
                                    "low, "
                                    "close, "
                                    
                                    "SMA)"
    
                                    "VALUES (%s, %s, %s, %s, "
                                    "%s, %s, %s, %s, %s, %s, "
                                    "%s, %s, '', '', '', '', '') ",

                                    (
                                        symb_id,
                                        date_id,
                                        round(float(pair[0][date]['1a. open (USD)']), 3),
                                        round(float(pair[0][date]['1b. open (USD)']), 3),
                                        round(float(pair[0][date]['2a. high (USD)']), 3),
                                        round(float(pair[0][date]['2b. high (USD)']), 3),
                                        round(float(pair[0][date]['3a. low (USD)']), 3),
                                        round(float(pair[0][date]['3b. low (USD)']), 3),
                                        round(float(pair[0][date]['4a. close (USD)']), 3),
                                        round(float(pair[0][date]['4b. close (USD)']), 3),
                                        round(float(pair[0][date]['5. volume']), 3),
                                        round(float(pair[0][date]['6. market cap (USD)']), 3)
                                    )
                                    )
                    else:
                        pass
                        # print('exist')

                print('Crypto inserted\n')
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print('Crypto error ', e)


def main_crypto():
    cc = []

    dates_mass = []
    current_symb_date = []

    with conn:
        with conn.cursor() as cur:
            # finding all dates and inserting them to the list
            cur.execute('SELECT * FROM dates')
            for row in cur:
                if row not in dates_mass:
                    dates_mass.append(row)

    for code in ga.crypto_symbols:

        start_t = time.time()

        try:
            source = ga.get_crypto_curr(code)
            crypto_insertion(source, dates_mass, current_symb_date)
            cc += [code]
            print('Done!\n')
        except Exception as e:
            print('Crypto error in main' + str(e))

        end_t = time.time()

        sleep_t = 12 - (end_t - start_t)

        if sleep_t < 0:
            sleep_t = 1

        print('Gonna sleep for: ' + str(sleep_t) + ' seconds')
        time.sleep(sleep_t)

    print(cc)
