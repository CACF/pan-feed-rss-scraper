from bs4 import BeautifulSoup

class BBC_Scraper:
    def __init__(self, soup):
        self.soup = soup
        self.content = ""

    def extract_content(self):
        # Exclude <div> tags with specific attributes
        components = [
            {"data-component": "social-block"},
            {"data-component": "ad-slot"},
            {"data-component": "links-block"},
            {"data-component": "video-block"},
            {"data-testid": "video-page-player"},
        ]

        for component in components:
            for div in self.soup.find_all("div", component):
                div.decompose()
        all_tags = self.soup.find_all(["p", "h2"])
        for tag in all_tags:
            self.content += tag.get_text().strip() + "\n"
        return self.content
    