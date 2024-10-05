import http.client
import json

currency_pairs = [
    ("USD", "UAH"), ("USD", "GBP"), ("USD", "JPY"), ("USD", "AUD"), ("USD", "CAD"),
    ("EUR", "GBP"), ("EUR", "JPY"), ("EUR", "AUD"), ("EUR", "CAD"), ("GBP", "JPY"),
    ("GBP", "AUD"), ("GBP", "CAD"), ("JPY", "AUD"), ("JPY", "CAD"), ("AUD", "CAD"),
    ("USD", "CHF"), ("EUR", "CHF"), ("GBP", "CHF"), ("AUD", "CHF"), ("CAD", "CHF")
]

def get_exchange_rate(base_currency, target_currency):
    conn = http.client.HTTPSConnection("v6.exchangerate-api.com")

    api_key = "87a72cf0b5259f1d1fb73dac"
    endpoint = f"/v6/{api_key}/latest/{base_currency}"
    conn.request("GET", endpoint)

    response = conn.getresponse()
    data = response.read()

    rates = json.loads(data)

    if response.status == 200:
        exchange_rate = rates['conversion_rates'].get(target_currency)
        if exchange_rate:
            return exchange_rate
        else:
            print(f"Немає даних для валюти {target_currency}.")
            return None
    else:
        print(f"Помилка отримання даних: {response.status} {response.reason}")
        return None

    conn.close()

def print_exchange_rates():
    for base_currency, target_currency in currency_pairs:
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        if exchange_rate:
            print(f"Курс {base_currency} до {target_currency}: {exchange_rate}")

print_exchange_rates()
