from  urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urlib.request\
        .urlopen(self.site)
        html = r.read()
