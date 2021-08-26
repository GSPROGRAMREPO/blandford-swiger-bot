def traverse_data(candle_data):

    # event = [event_date, buyOrSaleFlag, candlePrice, candle.ticker, candle.id]
    event_list = []

    # There needs to be a minimum ammount of time alloted to only collect data
    # before trading the asset can be considered

    # The event recorded occurs the following day of an event signal
    # Obviously when considering the closing data of a stock as a signal to buy
    # It is too late to make a purchase at that days price

    trading_start_date = 45
    research_start_date = 0


    for index, candle in enumerate(candle_data):

        if index >= trading_start_date:

            if is_buy_trigger(candle_data, index):
                candle_data[index].event_type = 0
                event_list.append(candle_data[index])

            if is_sell_trigger(candle_data, index):
                candle_data[index].event_type = 1
                event_list.append(candle_data[index])

    return event_list


def is_buy_trigger(candle_data, index):

    #The Greater the signal line value the less likely a buy event will occur
    signal_line = .9
    avg_rsi = candle_data[index].rsi_avg_low
    current_rsi = candle_data[index].rsi
    normalized_value = ((current_rsi + avg_rsi + 30) / 3)

    # If the current_rsi dips belows the average of the previous 10 rsi_lows than
    # This is a buy signal
    if (normalized_value / current_rsi) > signal_line:
        return True
    else:
        return False


def is_sell_trigger(candle_data, index):

    #The Greater the signal line value the more likely a sell event will occur
    signal_line = .9
    avg_rsi = candle_data[index].rsi_avg_high
    current_rsi = candle_data[index].rsi

    # If the current_rsi rises above the average of the previous 10 rsi highs than
    # This is a sell signal
    if (avg_rsi / current_rsi) < signal_line:
        return True
    else:
        return False

