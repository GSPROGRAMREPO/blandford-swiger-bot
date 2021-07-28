'''

The Goal of the code belows is to calculate RSI
The Formula for RSI is as follows

                  100
    RSI = 100 - --------
                 1 + RS

    RS = Average Gain / Average Loss

    First Average Gain = Sum of Gains over the past 14 periods / 14.
    First Average Loss = Sum of Losses over the past 14 periods / 14

    This RSI calculation is based on 14 periods.
    Losses are expressed as positive values, not negative values.

'''


def set_candle_gain(candles):

    for index, candle in enumerate(candles):

        if index > 1:
            previous_candle = candles[index - 1]
            gain = round(float(candle.candle_close) - float(previous_candle.candle_close), 3)

            if gain > 0:
                candles[index].candle_gain = gain

            if gain < 0:
                candles[index].candle_loss = gain * -1

            else:
                candle.candle_loss = 0.0


def set_candle_average_gain(candles):
    data_set = candles
    data_set.pop(0)
    data_set.pop(0)

    for index, candle in enumerate(data_set):
        calculate_average_gain(data_set[index:index + 14])


def calculate_average_gain(candles):
    total_gain = 0.0
    total_loss = 0.0
    previous_candle = len(candles)-2

    if candles[previous_candle].candle_average_gain == 0.0:
        for index, candle in enumerate(candles):
            if candle.candle_gain > 0:
                total_gain += candle.candle_gain
            else:
                total_loss += candle.candle_loss

        candles[len(candles)-1].candle_average_gain = total_gain / 14
        candles[len(candles)-1].candle_average_loss = total_loss / 14

    else:
        candles[len(candles)-1].candle_average_gain = (candles[previous_candle].candle_average_gain*(14-1) +
                                                       candles[len(candles) - 1].candle_gain)/14
        candles[len(candles) - 1].candle_average_loss = (candles[previous_candle].candle_average_loss * (14 - 1) +
                                                         candles[len(candles) - 1].candle_loss) / 14

        # print(candles[len(candles) - 1].candle_date + " " + str(candles[len(candles) - 1].candle_average_gain))
        # print(candles[len(candles) - 1].candle_date + " " + str(candles[len(candles) - 1].candle_average_loss))

    return


def set_candle_rs(candles):

    for candle in candles:
        if candle.candle_average_gain != 0.0:
            candle.candle_rs = candle.candle_average_gain / candle.candle_average_loss


def set_candle_rsi(candles):

    for candle in candles:
        if candle.candle_rs != 0.0:
            candle.candle_rsi = 100-(100/(candle.candle_rs + 1))
            print(candle.candle_date + " RSI:" + str(candle.candle_rsi))
