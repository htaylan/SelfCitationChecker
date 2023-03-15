Can you make this code OOP based and more professional

import re 
import os 
import requests
from bs4 import BeautifulSoup

def get_researcher_tables(url):
    html = requests.get(url, headers=headers, proxies=proxies).text
    soup = BeautifulSoup(html)
    return soup
  
  def get_prof_names_from_uni(soup):
    whole_table = str(soup.find('div', attrs={"id" : "collapse-1652"}))
    return whole_table
 def get_postdoc_names_from_uni(soup):
    whole_table = str(soup.find('div', attrs={"id" : "collapse-1653"}))
    return whole_table
  
  def get_phd_names_from_uni(soup):
    whole_table = str(soup.find('div', attrs={"id" : "collapse-1656"}))
    return whole_table
  
  def firstname(table):
    pattern_firstname = '"MX_FIRSTNAME":"(.*?)",'
    firstname = re.findall(pattern_firstname,table)
    return firstname
  
  def lastname(table):
    pattern_lastname = '"MX_LASTNAME":"(.*?)",'
    lastname = re.findall(pattern_lastname,table)
    return lastname
  
  def phd_firstname(table):
    pattern_firstname = 'MX_FIRSTNAME&quot;:&quot;(.*?)&quot'
    firstname = re.findall(pattern_firstname, table)
    return firstname
  
  def phd_lastname(table):
    pattern_lastname = 'MX_LASTNAME&quot;:&quot;(.*?)&quot' 
    lastname = re.findall(pattern_lastname, table)
    return lastname
  
  
