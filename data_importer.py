import yfinance as yf

# tickers remove WRK ETSY CTLT PAYC


ticker_list = ['AAPL', 'MSFT', 'AMZN', 'FB', 'GOOGL',
               'AXP','SYY','GD','WEC','GL','A',
           'GOOG', 'JNJ', 'JPM', 'V', 'UNH', 'PG', 'NVDA',
           'DIS', 'MA', 'HD', 'BAC', 'VZ', 'ADBE', 'NFLX',
           'INTC', 'T', 'MRK', 'PFE', 'WMT', 'CRM', 'TMO',
           'ABT', 'PEP', 'KO', 'XOM', 'CSCO', 'ABBV', 'NKE',
           'AVGO', 'QCOM', 'CVX', 'ACN', 'COST', 'MDT', 'MCD',
           'NEE', 'TXN', 'DHR', 'HON', 'UNP', 'LIN', 'BMY',
           'WFC', 'C', 'LLY', 'PM', 'SBUX', 'LOW',
           'ORCL', 'IBM', 'UPS', 'BA', 'MS', 'BLK', 'RTX',
           'CAT', 'GS', 'NOW', 'GE', 'MMM', 'INTU', 'CVS',
           'AMT', 'TGT', 'ISRG', 'DE', 'BKNG', 'SCHW', 'MU',
           'AMAT', 'LMT', 'FIS', 'TJX', 'ANTM', 'MDLZ', 'SYK',
           'CI', 'ZTS', 'SPGI', 'GILD', 'MO', 'LRCX',
           'BDX', 'ADP', 'CSX', 'CME', 'PLD', 'CB', 'CL', 'TFC',
           'ADSK', 'USB', 'PNC', 'DUK', 'FISV', 'CCI', 'ICE',
           'SO', 'NSC', 'APD', 'VRTX', 'ITW', 'SHW', 'D', 'FDX',
           'DD', 'HUM', 'EL', 'ADI', 'MMC', 'ECL', 'EW', 'PGR',
           'GM', 'DG', 'BSX', 'NEM', 'ETN', 'COF', 'REGN', 'EMR',
           'COP', 'AON', 'WM', 'MCO', 'NOC', 'FCX', 'ROP', 'KMB',
           'ROST', 'CTSH', 'KLAC', 'TEL', 'BAX', 'EXC', 'EA', 'APH',
           'AEP', 'APTV', 'STZ', 'MCHP', 'BIIB', 'CMG',
            'LHX', 'MET', 'JCI', 'TT', 'BK', 'XLNX',
            'PH', 'PPG', 'GIS', 'CMI', 'F', 'HPQ', 'TRV', 'AIG',
            'TROW', 'EBAY', 'MAR', 'SLB', 'SRE', 'MNST', 'XEL', 'EOG',
            'ALXN', 'ORLY', 'ALL', 'PSA', 'ZBH', 'WBA', 'PRU',
            'YUM', 'PSX', 'CTAS', 'PCAR', 'ES', 'ROK', 'DFS', 'BLL',
            'MCK', 'PAYX', 'AFL', 'ADM', 'MSI', 'AZO', 'MPC', 'AME',
            'FAST', 'SWK', 'KMI', 'PEG', 'GLW', 'VFC', 'LUV', 'SPG',
            'STT', 'DLTR', 'ENPH', 'WELL', 'WMB', 'DAL',
            'WY', 'LYB', 'BBY', 'CLX', 'KR', 'CERN', 'VLO', 'ED', 'AMP',
            'MKC', 'EIX', 'DTE', 'DHI', 'VIAC', 'WST', 'FITB', 'VRTS',
            'HSY', 'EFX', 'AVB', 'ZBRA', 'PXD', 'TER', 'VMC', 'PPL',
            'LH', 'LEN', 'CBRE', 'IP', 'RSG','NTRS', 'KSU', 'VRSN',
            'EQR', 'XYL', 'ODFL', 'EXPE', 'MLM',
            'URI', 'LVS', 'TSN', 'ETR', 'MTB', 'CDW', 'DOV', 'AEE', 'GRMN',
            'OKE', 'HIG', 'KEY', 'GWW', 'HAL', 'PKI', 'VTR', 'TYL',
            'OXY', 'TSCO', 'STE', 'NUE', 'RF', 'AKAM', 'HES', 'DGX',
            'CMS', 'CAH', 'CAG', 'KMX', 'AES', 'ABC', 'WAT', 'DRI',
            'FE', 'EXPD', 'CTXS', 'FMC', 'NDAQ', 'POOL', 'K', 'CCL', 'PEAK',
            'DPZ', 'ESS', 'GPC', 'J', 'HBAN', 'EMN', 'NTAP', 'MAS',
            'NVR', 'OMC', 'RCL', 'AVY', 'BIO', 'STX', 'SJM', 'PFG', 'TDY',
            'CINF', 'CHRW', 'HRL', 'BXP', 'IFF', 'XRAY', 'NLOK', 'HAS',
            'WHR', 'PHM', 'CNP', 'TXT', 'ALLE', 'UHS', 'DVN', 'L', 'HWM',
            'LNC', 'IPG', 'SNA', 'WU', 'WRB', 'TAP', 'PNR',
            'CF', 'NRG', 'DVA', 'PNW', 'CMA', 'MHK', 'NWL', 'NI', 'AIZ',
            'IRM', 'ZION', 'JNPR', 'PVH', 'NLSN', 'RHI', 'SEE', 'NWSA',
            'COG', 'BEN', 'IVZ', 'KIM', 'APA', 'PRGO', 'MRO',
            'HST', 'BWA', 'TPR', 'CPB',
            'LB', 'WYNN', 'PWR','LYV']

# Tickers are added to the pool at the beginning of the following year to account for
# any large jumps due to being added to the SnP
tickers_added_2016 = ['HCA', 'SWKS', 'HSIC', 'EQIX', 'HBI', 'AAL', 'O', 'QRVO',
                      'JBHT', 'KHC', 'AAP', 'PYPL', 'ATVI', 'UAL', 'FOX','NWS',
                      'VRSK', 'HPE', 'SYF', 'ILMN', 'CHD']
tickers_added_2017 = ['WLTW','EXR','CFG','FRT','AWK','UDR','CNC','HOLX','UA',
                      'ULTA', 'GPN','ALK','DLR','LKQ','AJG','TDG','FBHS','ALB',
                      'LNT','FTV','MTD','CHTR','COO','MAA']
tickers_added_2018 = ['IDXX','INCY','CBOE','REG','DISH','SNPS','ARE','RJF','DXC',
                      'IT','INFO','ALGN','ANSS','RE','HLT','BKR','AOS','DRE','MGM',
                      'PKG','RMD','IQV','SBAC','CDNS','NCLH','AMD']
tickers_added_2019 = ['HII','IPGP','SIVB','TTWO','MSCI','ABMD','EVRG','TWTR','BR',
                      'FLT','CPRT','ANET','ROL','FTNT','KEYS','JKHY','FANG','LW',
                      'MXIM','CE']

'''
for ticker in ticker_list:
    data = yf.download(ticker, start="2013-10-01", end="2020-01-1", threads=True)
    data.to_csv(('info\\' + ticker + '.csv'))
'''