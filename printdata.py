def print_gain_data(candles):

    for candle in candles:

        if candle.candle_gain > 0:
            print(candle.candle_date + ' ' + str(candle.candle_gain))

        else:
            print(candle.candle_date + ' ' + str(candle.candle_loss))