def make_trades(possible_trades):
    quant = 15
    a_buy = '0'
    a_sell = '1'
    price = 2
    ticker = 0
    purse = 100000
    current_holdings = []
    trade_events = sorted(generate_event_list(possible_trades), key=lambda x: x[1])

    for trade in trade_events:
        if trade[3] == a_buy and quant*trade[price] < purse:
            current_holdings.append(trade[ticker])
            purse = purse - quant*trade[price]
            print(trade)
        if trade[3] == a_sell and trade[ticker] in current_holdings:
            purse = purse + quant*trade[price]
            current_holdings.remove(trade[ticker])
            print(trade)
        print(purse)
    print(current_holdings)


def calculate_buy_ammount(max, price):
    number_to_buy = 0
    total = 0
    while total < max:
        total = total + price
        number_to_buy = number_to_buy + 1

    return number_to_buy


def generate_event_list(possible_trades):
    event_list = []

    for trade in possible_trades:
        buy_event = []
        sell_event = []
        '''trade = [purchase_date, purchase_price, selling_date, 
        selling_price, profit, candle.candle_ticker]'''
        buy_event.append(trade[5])
        buy_event.append(trade[0])
        buy_event.append(trade[1])
        buy_event.append('0')
        event_list.append(buy_event)
        sell_event.append(trade[5])
        sell_event.append(trade[2])
        sell_event.append(trade[3])
        sell_event.append('1')
        event_list.append(sell_event)

    return event_list
