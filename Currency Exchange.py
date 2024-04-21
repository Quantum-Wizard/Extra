import requests

# Fetch exchange rates from the API
def fetch_data():
    response = requests.get('https://open.er-api.com/v6/latest/USD')
    response.raise_for_status()  # Ensure we got a valid response
    return response.json()

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    data = fetch_data()
    try:
        from_rate = data['rates'][from_currency]
        to_rate = data['rates'][to_currency]
    except KeyError:
        print("Invalid currency code. Please try again.")
        return None

    # Calculate the converted amount
    converted_amount = (amount / from_rate) * to_rate
    return converted_amount

# Get user input
try:
    amount = float(input("Enter the amount you want to convert: "))
except ValueError:
    print("Invalid amount. Please try again.")
else:
    from_currency = input("Enter the currency you want to convert from (e.g., EUR): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., GBP): ").upper()

    # Perform the conversion
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is approximately {converted_amount} {to_currency}")
