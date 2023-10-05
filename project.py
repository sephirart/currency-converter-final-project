# -- IDEA: --
# A currency converter that uses an external API
#

# -- REQUIREMENTS: --
# [x] name is project.py
# [x] main function
# [] 3 functions minimum
# [] test_project.py file that tests project.py
# [x] all libraries in requirements.txt, one per line

###################################################################

# Import libraries
from requests import get
from pprint import PrettyPrinter

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


# Main function
def main():
    req_currency()


if __name__ == "__main__":
    main()
