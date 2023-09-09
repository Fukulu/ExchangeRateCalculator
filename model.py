import requests
import pandas as pd

exchange_rate_api_key = "YOUR_API_KEY_FROM_EXCHANGERATE-API.COM"
main_currency = "TRY"
main_amount = 0.0
requested_currency = "USD"
result_currency = 0.0

def make_request():
    url = f"https://v6.exchangerate-api.com/v6/{exchange_rate_api_key}/latest/{main_currency}"
    response = requests.get(url)
    exchange_data = response.json()
    return exchange_data["conversion_rates"][requested_currency]


df = pd.read_csv("currency.csv", delimiter=';')
currency_list = df["currency_code"]
newdf = df.drop(columns="currency_code")
newdf.set_index(currency_list, inplace=True)

def get_exp(currency):
    currency_name = newdf.loc[currency]["currency_name"]
    country_name = newdf.loc[currency]["country_name"]
    return "Country Name: " + country_name + " , " + "Currency Name: " + currency_name