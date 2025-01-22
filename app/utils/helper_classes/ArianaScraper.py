from bs4 import BeautifulSoup
import requests


class Ariana_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self):
        content = ""
        # Find the div with id="mvp-content-main"
        main_content = self.soup.find(id="mvp-content-main")
        if main_content:
            # Find all p tags within this div
            all_p_tags = main_content.find_all("p")
            for p_tag in all_p_tags:
                content += p_tag.get_text().strip() + "\n"
        return content
