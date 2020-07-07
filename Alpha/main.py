import Alpha.crypto_insert as crpdf
import Alpha.curr_insert as crdf
import Alpha.get_symbols_and_date_defs as cndf
import Alpha.tech_insert as tcdf
import Alpha.create_main_table


def main():

    cndf.main_symbols()    # create&insert symbols
    cndf.main_dates()       # create&insert dates

    Alpha.create_main_table.create()  # create main table

    crpdf.main_crypto()     # insert crypto
    crdf.main_curr()        # insert curr
    tcdf.main_tech()        # insert tech


if __name__ == '__main__':
    main()
