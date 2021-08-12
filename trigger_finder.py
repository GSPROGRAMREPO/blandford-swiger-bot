

def is_buy_trigger(candle_data, index):
    rsi_value = candle_data[index].candle_rsi

    if (rsi_value < 40 and rsi_value != 0.0):
        #and candle_data[index].candle_macd > candle_data[index-1].candle_macd:

        return True
    else:
        return False

    return


def is_sell_trigger(candle_data, index):
    if candle_data[index].candle_rsi > 80:
        return True
    else:
        return False

    return


def traverse_data(candle_data):

    holding_stock = False
    trade_list = []
    purchase_price = 0.0
    selling_price = 0.0

    for index, candle in enumerate(candle_data):
        if holding_stock is False and is_buy_trigger(candle_data, index):
            holding_stock = True
            purchase_price = float(candle.candle_high)
            purchase_date = candle.candle_date

        if is_sell_trigger(candle_data, index) and holding_stock is True:
            holding_stock = False
            selling_price = float(candle.candle_low)
            selling_date = candle.candle_date

        if purchase_price != 0.0 and selling_price != 0.0:
            profit = selling_price - purchase_price
            trade = [purchase_date, purchase_price, selling_date, selling_price, profit, candle.candle_ticker]
            trade_list.append(trade)
            purchase_price = 0
            selling_price = 0
    return trade_list
