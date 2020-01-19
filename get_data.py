import requests

# Make a request to API HTTP protocol
request = requests.get(
    'https://free.currconv.com/api/v7/convert?q=BTC_USD,USD_BRL,EUR_BRL&compact=ultra&apiKey=ba0d2d89dc605de067c9')
# turn that Response data in a dict type by json method
address_data = request.json()


def get_BTC_USD():
    return address_data['BTC_USD']


def get_USD_BRL():
    return str(address_data['USD_BRL'])


def get_EUR_BRL():
    return address_data['EUR_BRL']
