# Currency Converter

### Basic Info

Video Demo (YT link): https://youtu.be/wBecOf98JOI
- Quick description: a currency converter based on free API from Free Curr Conv.
- Course: CS50 Python
- Motivation: I wanted to create something that tested what I had learned in the course by adding an external API and multiple functions while still meeting the requirements for the final project. 

### How it works

#### Structure
The structure of the program is the following: 4 functions and the main function.

The idea is that the main function prints a welcome message, listing out all possible commands (getting the list of currencies available for conversion, getting the convert rate between two currencies and converting a specific amount from one currency to the other) and then calling each function based on the command given.

#### Functions
Before the functions there is a section where I have imported the libraries:
 - requests, to be able to access the information in the API
 - pprint, specifically PrettyPrinter to format the JSON to make it more readable
 - sys
and then put my API key. 

I was very lucky to be able to get a free one and I had to wait only 8 days to get it, the process was really fast. Since I don't have a premium account it does expire monthly, but it was more than enough for me to complete this project, no matter my busy schedule. 

After, there is the first function, named "req_currency".

What I wanted to implement with this function was to get from the API the list of all results in the JSON file and format it in a readable easy way, by using Pretty Printer and the sort method.

The second function is "print_currency". 

It takes in the "currency" argument, passed by the req_currency. 
It takes and lists out to the user all currencies by displaying their id, name and symbol. Some currencies lack the last one so the default one is none. 

The third function is "get_rate".

It takes in two arguments, called "currency1" and "currency2", given from the main function as user input (in the main function it gets stripped of eventual excess characters and is converted to uppercase in case the user didn't write it correctly).
It looks in the JSON for the rate and then returns the rate itself as a float after displaying the result for the user.

The last function is "convert". 

It takes in three arguments: "currency1", "currency2" and "amount", given from the main function as user input. 
It calls the "get_rate" function to get the conversion rate and then multiplies it by the amount given by the user, after checking if the amount is valid. 
It returns the converted amount after displaying a result message for the user. 

The main function displays a quick welcome message, listing out all possible commands of the program. Then gets the user's input and calls the various functions based on the commands inputted. The command "q" quits the program and the main function checks if a command is valid or not, displaying a message if invalid. 

### Testing
It's included in the repository a test_project.py file that imports the functions "get_rate" and "convert" to then be tested by the respective functions test_get_rate and test_covert. 

## Thank you for reading!
Seph
