class SingleCandle:

    candle_date = ''
    candle_open = 0.0
    candle_high = 0.0
    candle_low = 0.0
    candle_close = 0.0
    candle_adj_close = 0.0
    candle_volume = 0.0
    candle_gain = 0.0
    candle_loss = 0.0
    candle_average_gain = 0.0
    candle_average_loss = 0.0
    candle_rs = 0.0
    candle_rsi = 0.0


    def __init__(self, date, open, high, low, close, adj_close, volume):
        self.candle_date = date
        self.candle_open = open
        self.candle_high = high
        self.candle_low = low
        self.candle_close = close
        self.candle_adj_close = adj_close
        self.candle_volume = volume
        self.candle_macd = 0.0
        self.candle_rs = 0.0
        self.candle_rsi = 0.0
        self.candle_gain = 0.0
        self.candle_loss = 0.0


    def to_string(self):
        the_string = 'Date: ' + str(self.candle_date) + ' Open: ' \
                     + str(self.candle_open) + ' High: ' + str(self.candle_high) + ' Low: ' \
                     + str(self.candle_low) + ' Close: ' + str(self.candle_close) + ' Adj_close: ' \
                     + str(self.candle_close) + ' Volume ' + str(self.candle_volume)
        return the_string



