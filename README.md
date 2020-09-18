## Bitcoin Price Notification
    Bitcoin Price Notification is a Python script to notify user about latest Bitcoin prices in various intervals of time and also to send emergency notification when the rice drops below the given threshold value

**Module**
1. Sending latest updates of bitcoin through Telegram, gmail
1. Sending emergency notification to mobile through ifttt web service 

![Image](https://drive.google.com/file/d/1X51LX-JRq6_8eId_9SBHl7r_bLFNq2mg/view?usp=sharing)

**Implementation**

1. fetch the price of bitcoin through https://api.coindesk.com/v1/bpi/currentprice.json using *get* request 
1. create virtual Environment and import requests library
1. create 3 applets here https://ifttt.com/create/ , one for sending emerging notification to the mobile, another 2 applets for sending price update to gmail and telegram
1. go to https://ifttt.com/maker_webhooks and create unique url link for each event

### Notification 
1. If current price of the bitcoin is less than the Threshold price, then send *post* request to the webhook url along with current rice of bitcoin
2. for **gmail** and **telegram** store the previous bitcoin prices in regular time intervals in a list, and send it to gmail and telegram using webhook url of respective events



