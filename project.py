# -- IDEA: --
# A currency converter that uses an external API
# Gets the users input and cleans it up + error management
#

# -- REQUIREMENTS: --
# [x] name is project.py
# [x] main function
# [x] 3 functions minimum
# [] test_project.py file that tests project.py
# [x] all libraries in requirements.txt, one per line

###################################################################

# Import libraries
from requests import get
from pprint import PrettyPrinter
import sys

# Currency API and key(expires after a while- to renew)
BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

# Make the JSON pretty
printer = PrettyPrinter()


# FUNC1: Getting the JSON file and sort it
def req_currency():
    # make the correct link with what we have
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    link = BASE_URL + endpoint
    # get the JSON file
    response = get(link).json()
    # find the results dict
    results = response["results"]
    # format it in a list and sort it
    results = list(response.items())
    results.sort()
    # return sorted results
    return results


# FUNC2: Printing the currencies
def print_currency(currencies):
    for name, currency in currencies:
        # Get currency name and id
        curr_name = currency["currencyName"]
        curr_id = currency["id"]
        # Not all of them have a symbol in the JSON so give default
        curr_symbol = currency.get("currencySymbol", "")
        print(f"{curr_id} - {curr_name} - {curr_symbol}")


# FUNC3: Getting the convert rate
def get_rate(currency1, currency2):
    # Make correct link to get convert rate
    endpoint = (
        f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    )
    link = BASE_URL + endpoint
    # Get JSON file
    response = get(link).json()
    # return results converted in list
    exchange_rate = list(response.values())[0]
    return f"Exchange rate from {currency1} to {currency2} is: {exchange_rate}"


# FUNC4: Converting the currencies with convert rate
def convert(currency1, currency2, amount):
    get_rate(currency1, currency2)


# Main function
def main():
    # Get currencies -- trying to clean user's input
    curr1 = input("Please enter currency to be converted (ex. USD): ").upper().strip()
    curr2 = input("Please enter currency to covert to (ex. CAD): ").upper().strip()
    amount = input("Please enter amount: ")
    # Error Management
    if len(curr1) > 3 or len(curr2) > 3:
        sys.exit("Invalid currency")
    # Move on with everything else
    data = req_currency()
    print_currency(data)
    convert(curr1, curr2, amount)


if __name__ == "__main__":
    main()
