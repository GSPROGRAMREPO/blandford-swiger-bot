class SingleCandle:

    id = 0
    date = ''
    ticker = ''
    candle_open = 0.0
    high = 0.0
    low = 0.0
    close = 0.0
    candle_adj_close = 0.0
    volume = 0.0
    gain = 0.0
    loss = 0.0
    average_gain = 0.0
    average_loss = 0.0
    avg_price = 0.0
    rs = 0.0
    rsi = 0.0
    rsi_avg_high = 0.0
    rsi_avg_low = 0.0
    short_ema = 0.0
    long_ema = 0.0
    macd = 0.0
    avg_performance = 0.0
    event_type = 9
    shares_held = 0
    shares_sold = 0
    profit_gain = 0
    stop_loss_peak = 0
    stop_loss_peak_breached = False

    def __init__(self, date, open, high, low, close, adj_close, volume, ticker):
        self.date = date
        self.candle_open = open
        self.high = high
        self.low = low
        self.close = close
        self.candle_adj_close = adj_close
        self.volume = volume
        self.macd = 0.0
        self.rs = 0.0
        self.rsi = 0.0
        self.gain = 0.0
        self.loss = 0.0
        self.ticker = ticker
        self.event_type = 9
        self.id = 0
