"""A Simple Script for Extracting Data from a Webpage 
This script allows the user to extract data from a webapge and then export the data to a csv file with column(s).
"""
from types import NoneType
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

n_refresh_time = 1
s_url = 'https://autobot.tf/items/random'
s_file_name = 'index.csv'
s_user_agent = 'Mozilla/5.0'
print("::Preass 'ctrl+c' to stop the script after pressing your cursor focus here::")
n_line_count = 0


while n_line_count < 1000 :
  http_requester = urllib.request.Request(s_url,headers={'User-Agent': s_user_agent})
  html_content = urllib.request.urlopen(http_requester)
  html_parse = BeautifulSoup(html_content, 'html.parser')
  itemname = html_parse.find_all('h1')
  skutext = html_parse.find_all('h3')
  with open(s_file_name, 'a') as csv_file_pointer:
    csv_writer = csv.writer(csv_file_pointer, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row1,row2 in zip(itemname, skutext):
      csv_writer.writerow([f"item={row1.get_text().strip()}"])
      csv_writer.writerow([f"sku={row2.get_text().strip()}"])
  with open('items.txt', 'a') as itemname_file:
    for row1 in itemname:
      itemname_file.write(f"item={row1.get_text().strip()}\n")
  with open('sku.txt', 'a') as skuId_file:
    for row2 in skutext:
      skuId_file.write(f"sku={row2.get_text().strip()}\n")
  n_line_count += 1
  time.sleep(n_refresh_time)