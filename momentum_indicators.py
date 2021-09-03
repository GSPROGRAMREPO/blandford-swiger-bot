import datetime

def set_all_indicators(candle_list):
    set_candle_gain(candle_list)
    set_average_gain(candle_list)
    set_rs(candle_list)
    set_rsi(candle_list)
    set_ema(candle_list, 12)
    set_ema(candle_list, 26)
    set_macd(candle_list)
    set_avg_rsi_high(candle_list)
    set_avg_rsi_low(candle_list)
    set_candle_id(candle_list)
    set_candle_price(candle_list)

    return


def set_candle_id(candles):




    for index, candle in enumerate(candles):
        year = int(candle.date[0:4])
        month = int(candle.date[5:7])
        day = int(candle.date[8:])
        test_id = int(datetime.datetime(year, month, day, 0, 0, ).timestamp())
        candle.id = index
    return


def set_candle_price(candles):
    for index, candle in enumerate(candles):
        candle.avg_price = (float(candle.low) + float(candle.high)) / 2
    return


def set_candle_gain(candles):

    for index, candle in enumerate(candles):

        if index > 1:
            # print(candle.ticker)
            previous_candle = candles[index - 1]
            gain = round(float(candle.close) - float(previous_candle.close), 3)

            if gain > 0:
                candles[index].gain = gain

            elif gain < 0:
                candles[index].loss = gain * -1

            else:
                candle.loss = 0.0


def set_average_gain(candles):
    data_set = candles
    data_set.pop(0)
    data_set.pop(0)

    for index, candle in enumerate(data_set):
        calculate_average_gain(data_set[index:index + 14])


def calculate_average_gain(candles):
    total_gain = 0.0
    total_loss = 0.0
    previous_candle = len(candles)-2

    if candles[previous_candle].average_gain == 0.0:
        for index, candle in enumerate(candles):
            if candle.gain > 0:
                total_gain += candle.gain
            else:
                total_loss += candle.loss

        candles[len(candles)-1].average_gain = total_gain / 14
        candles[len(candles)-1].average_loss = total_loss / 14

    else:
        candles[len(candles)-1].average_gain = (candles[previous_candle].average_gain*(14-1) +
                                                       candles[len(candles) - 1].gain)/14
        candles[len(candles) - 1].average_loss = (candles[previous_candle].average_loss * (14 - 1) +
                                                         candles[len(candles) - 1].loss) / 14

    return


def set_rs(candles):

    for candle in candles:
        if candle.average_gain != 0.0:
            candle.rs = candle.average_gain / candle.average_loss


def set_rsi(candles):

    for candle in candles:
        if candle.rs != 0.0:
            candle.rsi = 100-(100/(candle.rs + 1))
            #print(candle.date + " RSI:" + str(candle.rsi))


def set_ema(candles, periods):
    short_ema_periods = 12
    long_ema_periods = 26
    smoothing = 2
    total = 0.0
    i = 0

    for candle in candles:

        if i < periods:
            total += float(candle.close)
            i = i + 1

        elif i == periods:
            if periods == short_ema_periods:
                candle.short_ema = total / periods

            if periods == long_ema_periods:
                candle.long_ema = total / periods
            i = i + 1

        else:
            if periods == short_ema_periods:
                candle.short_ema = float(candle.close) * (smoothing/(periods+1)) \
                                          + candles[i-1].short_ema*(1-(smoothing/(periods+1)))
            if periods == long_ema_periods:
                candle.long_ema = float(candle.close) * (smoothing / (periods + 1)) \
                                  + candles[i - 1].long_ema * (1 - (smoothing / (periods + 1)))
            i = i + 1
    return


def set_macd(candles):

    for candle in candles:
        if candle.short_ema != 0.0 and candle.long_ema != 0.0:
            candle.macd = candle.short_ema - candle.long_ema

    return


def set_avg_rsi_high(candles):

    rsi_highs = []
    length = 10

    for candle in candles:
        if len(rsi_highs) < length:
            rsi_highs.append(candle.rsi)
        else:
            min_value = min(rsi_highs)
            if candle.rsi > min_value:
                min_index = rsi_highs.index(min_value)
                rsi_highs.pop(min_index)
                rsi_highs.append(candle.rsi)
        candle.rsi_avg_high = sum(rsi_highs)/length

    return


def set_avg_rsi_low(candles):
    rsi_lows = []
    length = 10

    for candle in candles:
        if len(rsi_lows) < length:
            rsi_lows.append(40)
        else:
            max_value = max(rsi_lows)
            if candle.rsi < max_value and candle.rsi != 0:
                max_index = rsi_lows.index(max_value)
                rsi_lows.pop(max_index)
                rsi_lows.append(candle.rsi)

        candle.rsi_avg_low = sum(rsi_lows) / length

    return












