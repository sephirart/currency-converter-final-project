# Currency Converter Project

### Basic Info

Video Demo (YT link):  <URL HERE>
- Quick description: a currency converter based on free API from Free Curr Conv.
- Course: CS50 Python
- Motivation: I wanted to create something that tested what I had learned in the course by adding an external API and multiple functions while still meeting the requirements for the final project. 

### How it works

#### Structure
The structure of the program is the following: 4 functions and the main function.

The idea is that the main function prints a welcome message, listing out all possible commands (getting the list of currencies available for conversion, getting the convert rate between two currencies and converting a specific amount from one currency to the other) and then calling each function based on the command given.

#### The functions
Before the functions there is a section where I have imported the libraries:
 - requests, to be able to access the information in the API
 - pprint, specifically PrettyPrinter to format the JSON to make it more readable
 - sys
and then put my API key. 

I was very lucky to be able to get a free one and I had to wait only 8 days to get it, the process was really fast. Since I don't have a premium account it does expire monthly, but it was more than enough for me to complete this project, no matter my busy schedule. 

After, there is the first function, named "req_currency". 
What I wanted to implement with this function was to get from the API the list of all results in the JSON file and format it in a readable easy way, by using Pretty Printer and the sort method. This function doesn't get called by the main function but it's really helpful to get the initial information needed for the other functions. 


