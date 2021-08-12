import yfinance as yf

ticker_list = ['AMD', 'SHOP', 'NNDM', 'HD', 'OCGN', 'WMT', 'MMM',
               'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADBE', 'AAP',
               'AES', 'AFL', 'A', 'APD', 'AKAM', 'ALK', 'ALB', 'ARE',
               'ALGN','ALLE','LNT','ALL', 'MO','AMZN','AMCR',
               'AEE','AAL','AEP','AXP','AIG','AMT','AWK','AMP','ABC','AME',
               'AMGN','APH','ADI','ANSS','ANTM','AON','AOS','APA','AAPL',
               'AMAT','APTV','ADM','ANET','AJD','AIZ','T','ATO','ADSK',
               'ADP','ADSK','ADP','AVB','AVY','BKR','BLL','BAC',
               'BK','BAX','BDX','BBY','BIO','BIIB','BLK','BA',
               'BWA','BXP','BSX','BMY','AVGO','BR','CHRW','COG','CDNS',
               'CRZ','CPB','COF','CAH','KMX','CCL','CTLT','CAT',
               'CBOE','CBRE','CDW','CE','CNC','CNP','CERN','CF','CRL','SCHW',
               'CHTR','CVX','CB','CHD','CI','CINF','CSCO','C']


'''
for ticker in ticker_list:
    data = yf.download(ticker, start="2017-01-01", end="2020-01-01")
    data.to_csv(('info\\' + ticker + '.csv'))
'''