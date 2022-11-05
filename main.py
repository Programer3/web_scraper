"""A Simple Script for Extracting Data from a Webpage 
This script allows the user to extract data from a webapge and then export the data to a csv file with column(s).
"""# libraries
from types import NoneType
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

from click import open_file# Put your URL here
refresh_time = 1
while True:
    print(f"This prints every {refresh_time} seconds.")
    url = 'https://autobot.tf/items/random'# Fetching the html
    request = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    content = urllib.request.urlopen(request)# Parsing the html 
    parse = BeautifulSoup(content, 'html.parser')# Provide html elements' attributes to extract the data 
    itemname = parse.find_all('h1')# Extracting the item name
    skutext = parse.find_all('h3')# Extracting the item sku Id
    with open('index.csv', 'a') as csv_file:
      writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #   writer.writerow(['Title','Author'])
      for row1,row2 in zip(itemname, skutext):
        writer.writerow([f"item={row1.get_text().strip()}"]) 
        writer.writerow([f"sku={row2.get_text().strip()}"])
    with open('items.txt', 'a', newline='') as itemname_file:
      writer = csv.writer(itemname_file)
      for row1,row2 in zip(itemname, skutext):
        writer.writerow([f"item={row1.get_text().strip()}"])
    with open('sku.txt', 'a', newline='') as skuId_file:
      writer = csv.writer(skuId_file)
      for row1,row2 in zip(itemname, skutext):
        writer.writerow([f"sku={row2.get_text().strip()}"])    
    time.sleep(refresh_time) # Delay for 1 minute (60 seconds).