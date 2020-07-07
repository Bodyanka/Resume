from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

cc = CryptoCurrencies(key='QYL8KJPSQIWA07K4')
fx = ForeignExchange(key='QYL8KJPSQIWA07K4')
ts = TimeSeries(key='QYL8KJPSQIWA07K4')
ti = TechIndicators(key='QYL8KJPSQIWA07K4')

all_curr_symbols = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN',
                    'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF',
                    'CLP', 'CNH', 'CNY', 'COP', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB',
                    'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK',
                    'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS',
                    'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD',
                    'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN',
                    'NAD', 'NGN', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON',
                    'RSD', 'RUB', 'RUR', 'RWF', 'SAR', 'SBDf', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD',
                    'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU',
                    'UZS', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW',
                    'ZWL']

curr_symbols = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD',
                'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH',
                'CNY', 'COP', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP',
                'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
                'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD',
                'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO',
                'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK',
                'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP',
                'SLL', 'SOS', 'SRD', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH',
                'UGX', 'UYU', 'UZS', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']


all_crypto_symbols = ['2GIVE', '808', 'ABT', 'ABY', 'AC', 'ACT', 'ADA', 'ADT', 'ADX', 'AE', 'AEON', 'AGI', 'AGRS',
                      'AI', 'AID', 'AION', 'AIR', 'AKY', 'ALIS', 'AMBER', 'AMP', 'AMPL', 'ANC', 'ANT', 'APPC', 'APX',
                      'ARDR', 'ARK', 'ARN', 'AST', 'ATB', 'ATM', 'ATS', 'AUR', 'AVT', 'B3', 'BAT', 'BAY', 'BBR', 'BCAP',
                      'BCC', 'BCD', 'BCH', 'BCN', 'BCPT', 'BCX', 'BCY', 'BDL', 'BEE', 'BELA', 'BET', 'BFT', 'BIS',
                      'BITB', 'BITBTC', 'BITCNY', 'BITEUR', 'BITGOLD', 'BITSILVER', 'BITUSD', 'BIX', 'BLITZ', 'BLK',
                      'BLN', 'BLOCK', 'BLZ', 'BMC', 'BNB', 'BNT', 'BNTY', 'BOST', 'BOT', 'BQ', 'BRD', 'BRK', 'BRX',
                      'BTA', 'BTC', 'BTCD', 'BTCP', 'BTG', 'BTM', 'BTS', 'BTSR', 'BTX', 'BURST', 'BUZZ', 'BYC', 'BYTOM',
                      'C20', 'CANN', 'CAT', 'CCRB', 'CDT', 'CFI', 'CHAT', 'CHIPS', 'CLAM', 'CLOAK', 'CMP', 'CMT', 'CND',
                      'CNX', 'COFI', 'COSS', 'COVAL', 'CRBIT', 'CREA', 'CREDO', 'CRW', 'CSNO', 'CTR', 'CTXC', 'CURE',
                      'CVC', 'DAI', 'DAR', 'DASH', 'DATA', 'DAY', 'DBC', 'DBIX', 'DCN', 'DCR', 'DCT', 'DDF', 'DENT',
                      'DFS', 'DGB', 'DGC', 'DGD', 'DICE', 'DLT', 'DMD', 'DMT', 'DNT', 'DOGE', 'DOPE', 'DRGN', 'DTA',
                      'DTB', 'DYN', 'EAC', 'EBST', 'EBTC', 'ECC', 'ECN', 'EDG', 'EDO', 'EFL', 'EGC', 'EKT', 'ELA',
                      'ELEC', 'ELF', 'ELIX', 'EMB', 'EMC', 'EMC2', 'ENG', 'ENJ', 'ENRG', 'EOS', 'EOT', 'EQT', 'ERC',
                      'ETC', 'ETH', 'ETHD', 'ETHOS', 'ETN', 'ETP', 'ETT', 'EVE', 'EVX', 'EXCL', 'EXP', 'FCT', 'FLDC',
                      'FLO', 'FLT', 'FRST', 'FTC', 'FUEL', 'FUN', 'GAM', 'GAME', 'GAS', 'GBG', 'GBX', 'GBYTE', 'GCR',
                      'GEO', 'GLD', 'GNO', 'GNT', 'GOLOS', 'GRC', 'GRS', 'GRWI', 'GTC', 'GTO', 'GUP', 'GVT', 'GXS',
                      'HBN', 'HEAT', 'HMQ', 'HPB', 'HSR', 'HUSH', 'HVN', 'HXX', 'ICN', 'ICX', 'IFC', 'IFT', 'IGNIS',
                      'INCNT', 'IND', 'INF', 'INK', 'INS', 'INSTAR', 'INT', 'INXT', 'IOC', 'ION', 'IOP', 'IOST', 'IOTA',
                      'IOTX', 'IQT', 'ITC', 'IXC', 'IXT', 'J8T', 'JNT', 'KCS', 'KICK', 'KIN', 'KMD', 'KNC', 'KORE',
                      'LBC', 'LCC', 'LEND', 'LEV', 'LGD', 'LINDA', 'LINK', 'LKK', 'LMC', 'LOCI', 'LOOM', 'LRC', 'LSK',
                      'LTC', 'LUN', 'MAID', 'MANA', 'MAX', 'MBRS', 'MCAP', 'MCO', 'MDA', 'MEC', 'MED', 'MEME', 'MER',
                      'MGC', 'MGO', 'MINEX', 'MINT', 'MITH', 'MKR', 'MLN', 'MNE', 'MNX', 'MOD', 'MONA', 'MRT', 'MSP',
                      'MTH', 'MTN', 'MUE', 'MUSIC', 'MYB', 'MYST', 'MZC', 'NAMO', 'NANO', 'NAS', 'NAV', 'NBT', 'NCASH',
                      'NDC', 'NEBL', 'NEO', 'NEOS', 'NET', 'NLC2', 'NLG', 'NMC', 'NMR', 'NOBL', 'NOTE', 'NPXS', 'NSR',
                      'NTO', 'NULS', 'NVC', 'NXC', 'NXS', 'NXT', 'OAX', 'OBITS', 'OCL', 'OCN', 'ODEM', 'ODN', 'OF',
                      'OK', 'OMG', 'OMNI', 'ONION', 'ONT', 'OPT', 'OST', 'PART', 'PASC', 'PAY', 'PBL', 'PBT', 'PFR',
                      'PING', 'PINK', 'PIVX', 'PIX', 'PLBT', 'PLR', 'PLU', 'POA', 'POE', 'POLY', 'POSW', 'POT', 'POWR',
                      'PPC', 'PPT', 'PPY', 'PRG', 'PRL', 'PRO', 'PST', 'PTC', 'PTOY', 'PURA', 'QASH', 'QAU', 'QLC',
                      'QRK', 'QRL', 'QSP', 'QTL', 'QTUM', 'QWARK', 'R', 'RADS', 'RAIN', 'RBIES', 'RBX', 'RBY', 'RCN',
                      'RDD', 'RDN', 'REC', 'RED', 'REP', 'REQ', 'RHOC', 'RIC', 'RISE', 'RLC', 'RLT', 'RPX', 'RRT',
                      'RUFF', 'RUP', 'RVT', 'SAFEX', 'SALT', 'SAN', 'SBD', 'SBTC', 'SC', 'SEELE', 'SEQ', 'SHIFT', 'SIB',
                      'SIGMA', 'SIGT', 'SJCX', 'SKIN', 'SKY', 'SLR', 'SLS', 'SMART', 'SMT', 'SNC', 'SNGLS', 'SNM',
                      'SNRG', 'SNT', 'SOC', 'SOUL', 'SPANK', 'SPC', 'SPHR', 'SPR', 'SNX', 'SRN', 'START', 'STEEM',
                      'STK', 'STORJ', 'STORM', 'STQ', 'STRAT', 'STX', 'SUB', 'SWFTC', 'SWIFT', 'SWT', 'SYNX', 'SYS',
                      'TAAS', 'TAU', 'TCC', 'TFL', 'THC', 'THETA', 'TIME', 'TIX', 'TKN', 'TKR', 'TKS', 'TNB', 'TNT',
                      'TOA', 'TRAC', 'TRC', 'TRCT', 'TRIG', 'TRST', 'TRUE', 'TRUST', 'TRX', 'TUSD', 'TX', 'UBQ', 'UKG',
                      'ULA', 'UNB', 'UNITY', 'UNO', 'UNY', 'UP', 'URO', 'USDT', 'UTK', 'VEE', 'VEN', 'VERI', 'VIA',
                      'VIB', 'VIBE', 'VIVO', 'VOISE', 'VOX', 'VPN', 'VRC', 'VRM', 'VRS', 'VSL', 'VTC', 'VTR', 'WABI',
                      'WAN', 'WAVES', 'WAX', 'WCT', 'WDC', 'WGO', 'WGR', 'WINGS', 'WPR', 'WTC', 'WTT', 'XAS', 'XAUR',
                      'XBC', 'XBY', 'XCN', 'XCP', 'XDN', 'XEL', 'XEM', 'XID', 'XLM', 'XMG', 'XMR', 'XMT', 'XMY', 'XPM',
                      'XRL', 'XRP', 'XSPEC', 'XST', 'XTZ', 'XUC', 'XVC', 'XVG', 'XWC', 'XZC', 'XZR', 'YEE', 'YOYOW',
                      'ZCC', 'ZCL', 'ZCO', 'ZEC', 'ZEN', 'ZET', 'ZIL', 'ZLA', 'ZRX']

crypto_symbols = ['2GIVE', 'ABY', 'ACT', 'ADA', 'ADT', 'AGI', 'AID', 'AION', 'ALIS', 'AMPL', 'ANT', 'ARK', 'AST', 'ATB',
                  'ATM', 'AUR', 'AVT', 'B3', 'BAT', 'BCC', 'BCD', 'BCH', 'BFT', 'BITB', 'BLZ', 'BNB', 'BNT', 'BTC',
                  'BTG', 'BTS', 'BUZZ', 'BYTOM', 'C20', 'CANN', 'CHAT', 'CLOAK', 'CND', 'CNX', 'COSS', 'CTXC', 'CVC',
                  'DAI', 'DASH', 'DATA', 'DCR', 'DENT', 'DGB', 'DGD', 'DMD', 'DOGE', 'DRGN', 'DTA', 'DYN', 'EDG', 'EDO',
                  'EGC', 'EKT', 'ELF', 'EMB', 'EMC', 'ENJ', 'EOS', 'ETC', 'ETH', 'ETHOS', 'ETN', 'ETP', 'FRST', 'FUN',
                  'GAME', 'GAS', 'GBX', 'GCR', 'GNO', 'GNT', 'GRC', 'GRS', 'GTO', 'GVT', 'HMQ', 'HVN', 'ICX', 'IFT',
                  'INK', 'INT', 'IOP', 'IOST', 'IOTA', 'IOTX', 'IXC', 'IXT', 'KICK', 'KIN', 'KMD', 'KNC', 'LCC', 'LEND',
                  'LINDA', 'LINK', 'LKK', 'LOOM', 'LRC', 'LSK', 'LTC', 'LUN', 'MANA', 'MAX', 'MCO', 'MDA', 'MGO',
                  'MITH',
                  'MKR', 'MLN', 'MNX', 'MTN', 'NANO', 'NAS', 'NCASH', 'NEO', 'NET', 'NLC2', 'NMC', 'NMR', 'NPXS',
                  'NULS', 'NVC', 'OBITS', 'ODEM', 'OK', 'OMG', 'OMNI', 'ONION', 'ONT', 'PAY', 'PING', 'PIVX', 'PLBT',
                  'PLR', 'POA', 'POLY', 'POSW', 'POWR', 'PPC', 'PPT', 'PPY', 'PRG', 'PRO', 'QASH', 'QTUM', 'R', 'RADS',
                  'RBIES', 'RBY', 'RCN', 'RDD', 'RDN', 'REC', 'REP', 'REQ', 'RISE', 'RLC', 'RLT', 'RRT', 'SAN', 'SBTC',
                  'SC', 'SHIFT', 'SIB', 'SIGT', 'SKY', 'SLR', 'SNC', 'SNGLS', 'SNM', 'SNT', 'SPANK', 'SRN', 'START',
                  'STORJ', 'STORM', 'STQ', 'STRAT', 'STX', 'SUB', 'SYS', 'TAAS', 'TFL', 'THETA', 'TIME', 'TKN', 'TNB',
                  'TNT', 'TRST', 'TRUE', 'TRX', 'TUSD', 'USDT', 'UTK', 'VEE', 'VEN', 'VIA', 'VIB', 'VOISE', 'VPN',
                  'VRS', 'VSL', 'VTC', 'WAN', 'WAVES', 'WAX', 'WCT', 'WGO', 'WGR', 'WPR', 'WTC', 'XBY', 'XEM', 'XLM',
                  'XMG', 'XMR', 'XMT', 'XRL', 'XRP', 'XTZ', 'XVG', 'XZC', 'YOYOW', 'ZEC', 'ZEN', 'ZET', 'ZIL', 'ZRX']

tech_symbols = ['MSFT', 'AAPL', 'INTC', 'AMZN', 'CSCO', 'GOOG']


def get_techind(code):
    return ti.get_sma(code, interval='daily', time_period=2)


def get_curr(code):
    return fx.get_currency_exchange_daily(from_symbol=code, to_symbol="USD")


def get_crypto_curr(code):
    return cc.get_digital_currency_daily(symbol=code, market="USD")
