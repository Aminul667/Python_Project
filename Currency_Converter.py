# TODO: pip install forex-python
 
from forex_python.converter import CurrencyRates

# function to convert currency
def convert_currency(amount):
    currency_rate = CurrencyRates()

    frm = input("From: ").upper()
    to = input("To: ").upper()

    result = currency_rate.convert(frm, to, amount)

    print("From {} {} to {}: ".format(amount, frm, to))
    print(result)

amount = int(input("Enter the amount: "))
convert_currency(amount)


# ! try input -> 200, usd, inr