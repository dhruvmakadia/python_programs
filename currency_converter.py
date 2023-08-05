import requests

def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    params = {'symbols': target_currency, 'apikey': api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['rates'][target_currency]
    else:
        raise Exception(f"Failed to fetch exchange rate. Status code: {response.status_code}")

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual API key from ExchangeRatesAPI
    API_KEY = 'YOUR_API_KEY'
    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    try:
        exchange_rate = get_exchange_rate(base_currency, target_currency, API_KEY)
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.")
    except Exception as e:
        print(f"Error: {e}")
