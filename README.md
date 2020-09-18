## Bitcoin Price Notification
Bitcoin Price Notification is a Python script to notify user about latest Bitcoin prices in various intervals of time and also to send emergency notification when price drops below the given threshold value.

**Module**
1. Sending latest updates of bitcoin through Telegram, gmail.
1. Sending emergency notification to mobile through ifttt web service.


**Implementation**

1. fetch the price of bitcoin through https://api.coindesk.com/v1/bpi/currentprice.json using *get* request. 
1. create virtual Environment and import requests library.
1. create 3 applets here https://ifttt.com/create/ , one for sending emerging notification to the mobile, another 2 applets for sending price update to gmail and telegram.
1. go to https://ifttt.com/maker_webhooks and create unique url link for each event.
1. trigger the webhook url when bitcoin price drops below the threshold price or to send updates about latest bitcoin prices.

### Notification 
1. If current price of the bitcoin is less than the Threshold price, then send *post* request to the webhook url along with current price of bitcoin.
2. for **gmail** and **telegram** notifications, store the previous bitcoin prices in regular time intervals in a list, and send it to gmail and telegram using webhook url of respective events.

### Installation Guide
**step1**
* Download this Repository or clone it in to your machine

**step2**
* make sure you installed latest version of python 

**step3**
* Run command 
```python
$ python bitcoin_notifications.py --help
```
**step4**
* You see the below options
```python
Threshold_Price  int  Enter your Threshold price
currency_type   str   Enter your currency type
Notification_Type str Enter the Notification type 
```
**step5**
* Example:
```python
$ python bitcoin_notifications.py 10750 USD telegram
```
here 10750 is the threshold price we are setting, and USD is the type of currency in which we want to see the price, we have EUR, GBP also has options for currency, telegram is the notification type which we want, we have gmail also has option for notifications.

### Target Applications
1. Telegram
1. gmail
1. ifttt mobile notification

### Python Packages and Library Used
* Requests
* time
* argParser

### Technologies Used
* Python
* HTTPS
* Webhooks
* Notifications
    * Telegram
    * IFTTT App
    * gmail

### API Reference
* [Coindesk API](https://api.coindesk.com/v1/bpi/currentprice.json)
* [Ifttt API](https://ifttt.com/home)


