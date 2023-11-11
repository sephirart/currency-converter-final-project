# Currency Converter Project

### Basic Info

Video Demo (YT link):  <URL HERE>
Quick description: a currency converter based on free API from Free Curr Conv.
Course: CS50 Python
Motivation: I wanted to create something that tested what I had learned in the course by adding an external API and multiple functions while still meeting the requirements for the final project. 

### How it works

The structure of the program is the following: 4 functions and the main function.

Before the functions there is a section where I have imported the libraries:
 - requests, to be able to access the information in the API
 - pprint, specifically PrettyPrinter to format the JSON to make it more readable
 - sys

After, there is the first function, named "req_currency". I am looking to get from the free API, using my key, the complete list of all currencies available and return it to the user sorted. The goal
