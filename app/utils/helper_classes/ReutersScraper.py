import os
from random import randint
from bs4 import BeautifulSoup
from zenrows import ZenRowsClient

class ReutersScraper:
    def random_api_picker(self):
        api_list = os.environ.get("ZENROWS_API").split(",")
        random_api = api_list[randint(0,len(api_list)-1)]
        return random_api


    def load_page(self, url):
        client = ZenRowsClient(self.random_api_picker())
        response = client.get(url)
        return BeautifulSoup(response.text, 'html.parser')






## Commenting this code which does scrape correctly from reuters after opening links in browser. 
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# class ReutersScraper:    
#     def __init__(self):
#         self.driver = self.setup_driver()
    
#     def setup_driver(self):
#         options = Options()
#         options.page_load_strategy = 'eager'
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
#     def load_page(self, url):
#         self.driver.get(url)
#         return BeautifulSoup(self.driver.page_source, 'html.parser')
    
#     def close(self):
#         self.driver.quit()
