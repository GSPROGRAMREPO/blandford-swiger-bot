import events
import trade_maker
import data_exporter


def main():

    event_list, all_data = events.create_event_list()

    new_trader = trade_maker.Trader(event_list, all_data)

    new_trader.read_events()
    new_trader.make_report()

    data_exporter.export_all(new_trader.all_events)



if __name__ == "__main__":
    main()