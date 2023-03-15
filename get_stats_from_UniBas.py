import re 
import os 
import requests
from bs4 import BeautifulSoup

class ResearcherScraper:
    BASE_URL = 'https://example.com'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}
    PROXIES = {'http': os.getenv('HTTP_PROXY')}
    
    def __init__(self, uni_id):
        self.uni_id = uni_id
    
    def _get_soup(self, url):
        html = requests.get(url, headers=self.HEADERS, proxies=self.PROXIES).text
        return BeautifulSoup(html, 'html.parser')
    
    def _get_table(self, collapse_id):
        url = f'{self.BASE_URL}/tables?id={self.uni_id}&collapse={collapse_id}'
        soup = self._get_soup(url)
        table = str(soup.find('div', attrs={'id': f'collapse-{collapse_id}'}))
        return table
    
    def get_professor_names(self):
        table = self._get_table(1652)
        pattern_firstname = '"MX_FIRSTNAME":"(.*?)",'
        pattern_lastname = '"MX_LASTNAME":"(.*?)",'
        firstnames = re.findall(pattern_firstname, table)
        lastnames = re.findall(pattern_lastname, table)
        return list(zip(firstnames, lastnames))
    
    def get_postdoc_names(self):
        table = self._get_table(1653)
        pattern_firstname = '"MX_FIRSTNAME":"(.*?)",'
        pattern_lastname = '"MX_LASTNAME":"(.*?)",'
        firstnames = re.findall(pattern_firstname, table)
        lastnames = re.findall(pattern_lastname, table)
        return list(zip(firstnames, lastnames))
    
    def get_phd_names(self):
        table = self._get_table(1656)
        pattern_firstname = 'MX_FIRSTNAME&quot;:&quot;(.*?)&quot'
        pattern_lastname = 'MX_LASTNAME&quot;:&quot;(.*?)&quot'
        firstnames = re.findall(pattern_firstname, table)
        lastnames = re.findall(pattern_lastname, table)
        return list(zip(firstnames, lastnames))

