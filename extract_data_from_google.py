import os
import urllib.parse

import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests_html import HTML
from requests_html import HTMLSession
import streamlit as st


class GoogleSearch:
    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    )

    PROXIES = {"http": os.getenv("HTTP_PROXY")}

    def __init__(self, query):
        self.query = query

    def get_source(self, url):
        """Return the source code for the provided URL.

        Args:
            url (str): URL of the page to scrape.

        Returns:
            response (object): HTTP response object from requests_html.
        """
        try:
            session = HTMLSession()
            response = session.get(url, headers={"User-agent": self.USER_AGENT}, proxies=self.PROXIES)
            return response
        except requests.exceptions.RequestException as e:
            print(e)

    def get_results(self):
        query = urllib.parse.quote_plus(self.query)
        response = self.get_source("https://www.google.com/search?q=" + query)
        return response

    def parse_results(self, response):
        css_identifier_result = ".tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = ".yuRUbf a"
        css_identifier_text = ".IsZvec"
        results = response.html.find(css_identifier_result)
        output = []
        for result in results:
            item = {
                "title": result.find(css_identifier_title, first=True).text,
                "link": result.find(css_identifier_link, first=True).attrs["href"],
                "text": result.find(css_identifier_text, first=True).text,
            }
            output.append(item)
        return output

    def search(self):
        response = self.get_results()
        return self.parse_results(response)
    
    def get_researcher_stats(id):
    
        html = requests.get(f'https://scholar.google.com/citations?hl=en&user={id}', headers=headers, proxies=proxies)
        soup = BeautifulSoup(html.text, 'lxml')

        interests = soup.select_one('#gsc_prf_int').text

        for info in soup.select('.gsc_rsb'):

            cite_total = info.select_one('tr:nth-child(1) .gsc_rsb_sc1+ .gsc_rsb_std').text
            cite_last5 = info.select_one('tr:nth-child(1) .gsc_rsb_std+ .gsc_rsb_std').text
            h_total = info.select_one('tr:nth-child(2) .gsc_rsb_sc1+ .gsc_rsb_std').text
            h_last5 = info.select_one('tr:nth-child(2) .gsc_rsb_std+ .gsc_rsb_std').text
            i_total = info.select_one('tr~ tr+ tr .gsc_rsb_sc1+ .gsc_rsb_std').text
            i_last5 = info.select_one('tr~ tr+ tr .gsc_rsb_std+ .gsc_rsb_std').text
            #articles_num = info.select_one('.gsc_rsb_m_a:nth-child(1) span').text.split(' ')[0]

            years = [graph_year.text for graph_year in soup.select('.gsc_g_t')]
            citations = [graph_citation.text for graph_citation in soup.select('.gsc_g_a')]

            citation_data = []

            for year, citation in zip(years,citations):
                citation_data.append({
                  'year': year,
                  'citation': citation,
                  })   

        return cite_total, cite_last5, h_total, h_last5, i_total, i_last5
