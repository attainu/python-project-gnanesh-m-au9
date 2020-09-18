import requests
import time
from datetime import datetime
import argparse


class BitCoinNotifier:
    def __init__(self):
        self.BITCOIN_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        self.IFTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/PRTQU8G_SMaWPR58enTlp'

    # getting bitcoin prices
    def get_latest_bitcoin_price(self, currency_Entered):
        response = requests.get(self.BITCOIN_API_URL)
        response_json = response.json()
        return int(response_json['bpi'][currency_Entered]['rate_float'])

    # notifying through ifttt app, telegram, gmail
    def post_iftt_webhook(self, event, value, currency):
        data = {'value1': value, 'value3': " ", 'value2': currency}
        iftt_event_url = self.IFTT_WEBHOOKS_URL.format(event)
        requests.post(iftt_event_url, json=data)

    def main(self, Threshold_price, currency, noty_type):
        bitcoin_history = []
        while True:
            price = self.get_latest_bitcoin_price(currency)
            date = datetime.now()

            if price < Threshold_price:
                self.post_iftt_webhook('bitcoin_price_emergency', price, currency)

            print('Date : {}, Price : {}'.format(date.strftime("%d.%m.%Y %H:%M"), price), currency)
            bitcoin_history.append({'date': date, 'price': price, 'currency': currency})

            if len(bitcoin_history) == 5:
                if noty_type == "telegram":
                    self.post_iftt_webhook('bitcoin_price_update', self.format_bitcoin_history(bitcoin_history), currency)
                elif noty_type == "gmail":
                    self.post_iftt_webhook('bitcoin_price_update_2', self.format_bitcoin_history(bitcoin_history), currency)
                elif noty_type == "both":
                    self.post_iftt_webhook('bitcoin_price_update', self.format_bitcoin_history(bitcoin_history), currency)
                    self.post_iftt_webhook('bitcoin_price_update_2', self.format_bitcoin_history(bitcoin_history), currency)
                else:
                    print("Notification method is not valid,Please Enter correct notification method")
                    break

                bitcoin_history = []
            time.sleep(1)

    def format_bitcoin_history(self, bitcoin_history):
        rows = []
        for bitcoin_price in bitcoin_history:
            date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
            price = bitcoin_price['price']
            currency = bitcoin_price['currency']
            row = '{} : <b>{} {}</b>'.format(date, price, currency)
            rows.append(row)
        return '<br>'.join(rows)


if __name__ == "__main__":
    B1 = BitCoinNotifier()
    parser = argparse.ArgumentParser(description="Bitcoin notification")

    # getting the position arguments
    parser.add_argument("Threshold_price", nargs=1, metavar="Threshold_Price", type=int, help="Enter your Threshold price")
    parser.add_argument("currency", nargs=1, metavar="currency_type", type=str, help="Enter your currency type")
    parser.add_argument("noty_type", nargs=1, metavar="Notification_Type", type=str, help="Enter the Notification type you want")

    args = parser.parse_args()

    # function to run the position arguments
    if args.currency[0] == "USD":
        B1.main(args.Threshold_price[0], "USD", args.noty_type[0])
    elif args.currency[0] == "GBP":
        B1.main(args.Threshold_price[0], "GBP", args.noty_type[0])
    elif args.currency[0] == "EUR":
        B1.main(args.Threshold_price[0], "EUR", args.noty_type[0])
    else:
        print("Invalid Currency Type, please Enter correct Currency Type")
