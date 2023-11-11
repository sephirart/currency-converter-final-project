# -- IDEA: --
# A currency converter that uses an external API
# Gets the users input and cleans it up + error management
#

# -- REQUIREMENTS: --
# [x] name is project.py
# [x] main function
# [x] 3 functions minimum
# [x] test_project.py file that tests project.py
# [x] all libraries in requirements.txt, one per line

###################################################################

# Import libraries
from requests import get
from pprint import PrettyPrinter
import sys

# Currency API and key(expires after a while- to renew)
BASE_URL = "https://free.currconv.com/"
API_KEY = "ea05eec2f9d6d3994de5"

# Make the JSON pretty
printer = PrettyPrinter()


# FUNC1: Getting the JSON file and sort it
def req_currency():
    # make the correct link with what we have
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    link = BASE_URL + endpoint
    # get the JSON file + find results
    response = get(link).json()["results"]
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
    rate = list(response.values())[0]
    print(f"Exchange rate from {currency1} to {currency2} is: {rate}")
    return rate


# FUNC4: Converting the currencies with convert rate
def convert(currency1, currency2, amount):
    rate = get_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount. Please input a number.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


# Main function
def main():
    data = req_currency()

    # Welcome message and some commands
    print("Welcome to the Currency Converter!")
    print()
    print("Here are the commands: ")
    print()
    print("List -> list the different currencies")
    print("Convert -> convert from one currency to another")
    print("Rate -> get the exchange rate of two currencies")
    print()

    while True:
        # Getting command from user
        command = input("Enter a command (q to quit): ").strip().casefold()

        # Quit program
        if command == "q":
            break
        # List currencies
        elif command == "list":
            print_currency(data)
        # Convert currencies -- trying to clean user's input
        elif command == "convert":
            curr1 = (
                input("Please enter currency to be converted (ex. USD): ")
                .upper()
                .strip()
            )
            amount = input(f"Please enter amount in {curr1}: ")
            curr2 = (
                input("Please enter currency to covert to (ex. CAD): ").upper().strip()
            )
            # Error Management
            if len(curr1) > 3 or len(curr2) > 3:
                sys.exit("Invalid currency")

            convert(curr1, curr2, amount)
        # Get exchange rate
        elif command == "rate":
            curr1 = (
                input("Please enter currency to be converted (ex. USD): ")
                .upper()
                .strip()
            )
            curr2 = (
                input("Please enter currency to covert to (ex. CAD): ").upper().strip()
            )
            # Error Management
            if len(curr1) > 3 or len(curr2) > 3:
                sys.exit("Invalid currency")
            get_rate(curr1, curr2)
        # If the command is invalid
        else:
            print("Invalid command, please try again!")


if __name__ == "__main__":
    main()
