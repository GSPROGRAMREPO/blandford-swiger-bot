import csv
import data_importer
import momentum_indicators
from candle import SingleCandle as Cndl
import event_finder


def create_event_list():
    candle_list = []
    ticker_list = data_importer.ticker_list
    event_list = []
    all_data = {}

    for ticker in ticker_list:

        with open(('info\\' + ticker + '.csv'), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                candle_list.append(Cndl(row[0], row[1], row[2], row[3], row[4],
                                        row[5], row[6], ticker))

        # Add momentum based indicators not available via yahoo finance rsi, emas, ect.
        momentum_indicators.set_all_indicators(candle_list)

        # An event is the occurrence of specified values in certain fields.
        # EX: RSI > 80
        ticker_specific_event_list = event_finder.traverse_data(candle_list)

        #Add info to a total master list
        all_data[ticker] = candle_list.copy()

        # Empty the list as to iterate through the next set of data belonging to another ticker.
        candle_list.clear()

        # Add events that occured with a specific ticker to the list of all events
        for event in ticker_specific_event_list:
            event_list.append(event)

    sorted_event_list = sorted(event_list, key=lambda e: e.id)
    return sorted_event_list, all_data
