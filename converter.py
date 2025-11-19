from requests import get
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
import os
    

def get_currencies():
    response = get(BASE_URL, headers=headers).json()
    print(response['data'])
    currencies = response['data'].keys()
    print("List of currencies: ")
    for currency in currencies:
        print(currency, end=" ")
    print('\n')

    while True:
        user_currency1 = input("Enter the currency to be converted: ").upper()
        if user_currency1 in currencies:
            break
        else:
            print("Please enter a valid currency from the list")

    while True:
        user_currency2 = input("Enter the currency to be converted to: ").upper()

        if user_currency2 in currencies:
            break
        else:
            print("Please enter a valid currency from the list")
            
    while True:
        try:
            curr1_amt = round(float(input("Enter amount to be converted: ")), 2)

            if curr1_amt >= 0:
                break
            else:
                print("Please enter a valid currency from the list")
                 
        except ValueError:
            print("Please enter a valid number for the amount.")

    converted_amt = round(curr1_amt * response['data'][user_currency1] * response['data'][user_currency2], 2)
    
    print(f"{curr1_amt} {user_currency1} => {converted_amt} {user_currency2}")

if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

    headers = CaseInsensitiveDict()
    headers["apikey"] = API_KEY

    get_currencies()
