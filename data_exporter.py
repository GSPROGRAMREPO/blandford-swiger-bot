import csv
def export_all(list_of_events):
    data = list_of_events
    print(data)

    try:
        colomns_set = False
        filename = 'items.csv'
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for trade in data:
                if colomns_set == True:
                    writer.writerow([trade.date, trade.ticker, trade.event_type, trade.shares_held, trade.shares_sold,
                                     trade.avg_price, trade.rsi, trade.volume, trade.profit_gain])
                else:
                    writer.writerow(['Date', 'Ticker', 'Trade Type', 'Shares Bought', 'Shares Sold',
                                     'Price', 'RSI Value', 'Volume', 'Profit'])
                    colomns_set = True
    except BaseException as e:
        print('BaseException:', filename)
    else:
        print('Data has been loaded successfully !')



    return