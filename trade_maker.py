import stop_loss_indicators as sli

class Trader:
    '''

        A trade is an action taken based on the occurence of an event in a given list of trade events.
        An event is a list of values
        ex: ['20181016', 0, 124.8, 'CB'] [string, int, float, string]
        If event[1] == 0 That would be considered a buy event
        If event[1] == 1 That would be considered a sale event

    '''

    def __init__(self, event_list, all_data):
        self.cash = 100000
        self.event_list = event_list

        # The tickers_held list is a simple list of strings containing the ticker symbols of stocks
        # that have been bought but not yet sold.
        self.tickers_held = []

        # The ledger is a list of trades that have occurred either buy or sell
        self.ledger = []

        # All of the stock data as a dictionary with ticker symbols as key
        # allowing for the ledger to be updated as needed with current information.
        self.all_data = all_data

        # ledger_value is used to hold the total value of all the stocks held at when the bot reaches the end
        # of it's timeline.
        self.ledger_value = 0.0

        # missed_purchases is an int holding the total number of times a buy event wasn't acted upon
        # due to insufficient cash held
        self.missed_purchases = 0

        # Data to send to excel spread sheet
        self.all_events = []

        #
        self.longest_held_stock = []

    def read_events(self):

        for event in self.event_list:
            self.act_on_event(event)

        return

    def act_on_event(self, event):
        self.update_ledger_value(event)

        if event.event_type == 0 and event.ticker not in self.tickers_held:
            self.buy_stock(event)
            self.check_stop_losses(event)
            return

        elif event.event_type == 1 and event.ticker in self.tickers_held:
            self.sell_stock(event)
            return

    def buy_stock(self, event):

        # Retrieve information for purchase tomorrow
        date = event.id + 1
        ticker = event.ticker
        stock_purchased = self.all_data.get(ticker)[date]

        # Determine quantity based on price
        quantity = self.shares_to_purchase(stock_purchased.avg_price)

        if quantity > 0 and self.cash > (quantity*stock_purchased.avg_price)\
                and ticker not in self.tickers_held:

            stock_purchased.shares_held = quantity
            stock_purchased.event_type = 0

            # Add the stock to the ledger
            self.ledger.append(stock_purchased)

            # Add the ticker to the tickers_held
            self.tickers_held.append(stock_purchased.ticker)

            # Subtract cost from cash
            self.cash = self.cash - (quantity*stock_purchased.avg_price)

            self.record_to_event_list(stock_purchased)
        else:
            self.check_stop_losses(event)

    def sell_stock(self, event):

        # Retrieve information about the sale tomorrow
        date = event.id + 1
        ticker = event.ticker
        stock_to_sell = self.all_data.get(ticker)[date]
        price = stock_to_sell.avg_price

        # Find the purchase event in the ledger
        for i in self.ledger:
            if event.ticker == i.ticker:
                purchase_event = i
                event_index = self.ledger.index(i)
                purchase_cost = self.ledger.index(i)

        # Determine quantity based on quantity held
        quantity = purchase_event.shares_held
        purchase_cost = purchase_event.shares_held * purchase_event.avg_price

        # Add the price * quantity to the cash
        self.cash = self.cash + (price*quantity)

        # Remove the stock from the ledger
        self.ledger.pop(event_index)

        # Remove the stock ticker from tickers_held
        self.tickers_held.remove(event.ticker)

        stock_to_sell.shares_sold = quantity

        profit_gain = ((price*quantity) - purchase_cost)
        stock_to_sell.profit_gain = profit_gain

        self.record_to_event_list(stock_to_sell)


        days_held = stock_to_sell.id - purchase_event.id
        print(stock_to_sell.date + stock_to_sell.ticker + ': ' + str(days_held))


        return

    def check_stop_losses(self, event):
        # Go through current RSI values of stocks
        date = event.id

        for purchase_stock in self.ledger:
            current_stock = self.all_data.get(purchase_stock.ticker)[date]

            if sli.forty_five_day_stop_loss(current_stock, purchase_stock):
                self.sell_stock(current_stock)
                self.buy_stock(event)
                break

            if (sli.one_twenty_day_stagnation_stop_loss(current_stock, purchase_stock)):
                self.sell_stock(current_stock)
                self.buy_stock(event)
                break

            if sli.short_term_rsi_stop_loss(current_stock, purchase_stock):
                self.sell_stock(current_stock)
                self.buy_stock(event)
                break

            if sli.trailing_stop_loss(purchase_stock):
                self.sell_stock(current_stock)
                self.buy_stock(event)
                break

        return

    def shares_to_purchase(self, price):

        share_ratio = (self.cash + self.ledger_value) / 10
        return round(share_ratio/price, 0)

    def update_ledger_value(self, event):

        print(len(self.ledger))

        # Reset ledger_value to 0
        self.ledger_value = 0.0

        for stock in self.ledger:
            date = event.id
            ticker = stock.ticker
            quantity = stock.shares_held
            current_price = self.all_data.get(ticker)[date].avg_price
            self.ledger_value = self.ledger_value + (quantity*current_price)


            # For Trailing Stop loss
            if current_price > stock.stop_loss_peak:
                stock.stop_loss_peak = current_price

            elif ((current_price - stock.stop_loss_peak)/stock.stop_loss_peak) < -.05 and \
                    ((event.id - stock.id) > 120):
                stock.stop_loss_peak_breached = True


        return

    def make_report(self):
        print('Current Cash: ' + str(self.cash))
        print('Current Value in Stock: ' + str(self.ledger_value))
        print('Total: ' + str(self.cash + self.ledger_value))

    def record_to_event_list(self, event):

        self.all_events.append(event)

        return














