from bs4 import BeautifulSoup

class BBC_Scraper:
    def __init__(self, soup):
        self.soup = soup
        self.content = ""

    def extract_content(self):
        # Exclude <div> tags with specific attributes
        for div in self.soup.find_all("div", {"data-component": "links-block"}):
            div.decompose()
        for div in self.soup.find_all("div", {"data-component": "video-block"}):
            div.decompose()
        for div in self.soup.find_all("div", {"data-testid": "video-page-player"}):
            div.decompose()
        all_tags = self.soup.find_all(["p", "h2"])
        for tag in all_tags:
            self.content += tag.get_text().strip() + "\n"
        return self.content
    