import csv
import trade_maker
import data_importer
import moindicators
from candle import SingleCandle as Cndl
import trigger_finder


def main():

    candle_list = []
    trade_list = []
    ticker_list = data_importer.ticker_list

    for ticker in ticker_list:

        with open(('info\\' + ticker + '.csv'), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                candle_list.append(Cndl(row[0].replace('-', ''), row[1], row[2], row[3], row[4],
                                        row[5], row[6], ticker))

        moindicators.set_all_indicators(candle_list)

        trade_list.append(trigger_finder.traverse_data(candle_list))

        candle_list.clear()

    master_list = sorted(generate_master(trade_list), key=lambda x: x[0])
    trade_maker.make_trades(master_list)


def generate_report(master_list):
    for trade in master_list:
        print(trade[5] + ' Bought on: ' + trade[0] + ' for ' + str(trade[1]))
        print('Sold on: ' + trade[2] + ' for ' + str(trade[3]))
        print('Profit: ' + str(trade[4]))

    return


def generate_master(trade_list):
    master_list = []
    for ticker in trade_list:
        for trade in ticker:
            master_list.append(trade)

    return master_list


if __name__ == "__main__":
    main()
