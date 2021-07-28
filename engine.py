import csv
import moindicators
from candle import SingleCandle as Cndl


def main():

    candle_list = []

    with open('example.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            candle_list.append(Cndl(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    '''
    To calculate the RSI of a given candle you must pass in the candle and the previous 15 candles objects
    
    '''

    def add_momentum_data_to_candles():

        moindicators.set_candle_gain(candle_list)
        moindicators.set_candle_average_gain(candle_list)
        moindicators.set_candle_rs(candle_list)
        moindicators.set_candle_rsi(candle_list)

        return

    add_momentum_data_to_candles()


if __name__ == "__main__":
    main()
