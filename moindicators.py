def set_all_indicators(candle_list):
    set_candle_gain(candle_list)
    set_candle_average_gain(candle_list)
    set_candle_rs(candle_list)
    set_candle_rsi(candle_list)
    set_candle_ema(candle_list)
    set_candle_macd(candle_list)

    return

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
            #print(candle.candle_date + " RSI:" + str(candle.candle_rsi))


def set_candle_ema(candles):

    set_twelve_ema(candles)
    set_twentysix_ema(candles)

    return


def set_twelve_ema(candles):
    periods = 12
    smoothing = 2
    total = 0.0
    i = 0

    for candle in candles:
        if i < periods:
            total += float(candle.candle_close)
            i = i + 1
        elif i == periods:
            candle.candle_short_ema = total / periods
            i = i + 1
        else:
            candle.candle_short_ema = float(candle.candle_close) * (smoothing/(periods+1)) \
                                      + candles[i-1].candle_short_ema*(1-(smoothing/(periods+1)))
            i = i + 1
    return


def set_twentysix_ema(candles):

    periods = 26
    total = 0.0
    smoothing = 2
    i = 0

    for candle in candles:
        if i < periods:
            total += float(candle.candle_close)
            i = i + 1
        elif i == periods:
            candle.candle_long_ema = total / periods
            i = i + 1
        else:
            candle.candle_long_ema = float(candle.candle_close) * (smoothing/(periods+1)) \
                                      + candles[i-1].candle_long_ema*(1-(smoothing/(periods+1)))
            i = i + 1
            #print(candle.candle_date + ': ' + str(candle.candle_long_ema))
    return


def set_candle_macd(candles):

    for candle in candles:
        if candle.candle_short_ema != 0.0 and candle.candle_long_ema != 0.0:
            candle.candle_macd = candle.candle_short_ema - candle.candle_long_ema

    return

