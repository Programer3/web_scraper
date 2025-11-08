"""A Simple Script for Extracting Data from a Webpage 
This script allows the user to extract data from a webapge and then export the data to a csv file with column(s).
"""
# libraries
from types import NoneType
import urllib.request
import time as tm
from bs4 import BeautifulSoup
import csv

n_refresh_time = 1  # global variable for refresh time
s_url = 'https://autobot.tf/items/random'  # global variable for url (string)
s_file_name = 'index.csv'  # global variable for file name
s_user_agent = 'Mozilla/5.0'  # global variable for user agent
print("::Preass 'ctrl+c' to stop the script after pressing your cursor focus here::")
# global variable for line count (integer)(initial value is 0)
n_line_count = 0


while n_line_count < 10:  # loop for 10 times not 10 seconds as initially value of n_line_count is 0
    # print(f"This prints every {n_refresh_time} seconds.") #print refresh time optional.
    # global variable for request with url and user agent, User agent is to prevent 403 error.
    http_requester = urllib.request.Request(
        s_url, headers={'User-Agent': s_user_agent})
    # request sends a request to the url and returns a response object which is of type http.client.HTTPResponse
    # Parsing the html, Provide html elements' attributes to extract the data
    html_content = urllib.request.urlopen(http_requester)
    # content is a response object which is of type http.client.HTTPResponse. It contains the html of the webpage in bytes.
    # Parse the html content using BeautifulSoup
    html_parse = BeautifulSoup(html_content, 'html.parser')
    # parse is a BeautifulSoup object which contains the html of the webpage in a structured format.
    itemname = html_parse.find_all('h1')  # Extracting the item name
    # itemname is a list of BeautifulSoup objects which contains the item name in a structured format.
    skutext = html_parse.find_all('h3')  # Extracting the item sku Id
    # skutext is a list of BeautifulSoup objects which contains the item sku Id in a structured format.
    # open file in append mode, csv_file_pointer is a file object which points to the file's location in the memory.
    with open(s_file_name, 'a') as csv_file_pointer:
        # with here is a context manager which closes the file automatically after the code block is executed, so no need to close the file manually using close() method.
        # writer is a csv writer object which writes to the file pointed by csv_file_pointer and uses ',' as delimiter.
        csv_writer = csv.writer(
            csv_file_pointer, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # writer.writerow(['Title','Author'])
        # zip is a built-in function which takes two lists and returns a list of tuples where each tuple contains one element from each list. here row1 and row2 are tuples.
        for row1, row2 in zip(itemname, skutext):
            # the for loop iterates over the list of tuples and writes each tuple to the file.
            # writerow is a method of csv writer object which writes a row to the file.
            csv_writer.writerow([f"item={row1.get_text().strip()}"])
            csv_writer.writerow([f"sku={row2.get_text().strip()}"])
    # open('items.txt', 'a', newline='') newline='' is used to prevent extra blank lines in the file. It works because the default value of newline is '\n'.
    with open('items.txt', 'a') as itemname_file:
        # newline here is not a keyword argument, it is a positional argument. It has no effect if the file is opened in binary mode which is the default mode i.e. 'rb'.
        for row1 in itemname:
            # these row1 and row2 are tuples
            # usage of f-string
            itemname_file.write(f"item={row1.get_text().strip()}\n")
    with open('sku.txt', 'a') as skuId_file:
        for row2 in skutext:
            # insted of using newline='' we have used itemname_file.write(f"sku={row1.get_text().strip()}\n") to prevent extra blank lines in the file. \r is used to prevent extra blank lines in the file same as newline='' but it works only on windows.
            skuId_file.write(f"sku={row2.get_text().strip()}\n")
    n_line_count += 1
    # sleep delays the execution of the next line of code by the specified number of seconds.
    tm.sleep(n_refresh_time)

text_file = open("items.txt", "r")
print(text_file.read())
text_file.close()
