from bs4 import BeautifulSoup
import requests


class Livemint_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self) -> str:
        content = self.soup.find(
            "div",
            {"class": "storyPage_storyContent__m_MYl"},
        )

        if content:
            content = [
                elem.get_text(strip=True)
                for elem in content.find_all("div", class_="storyParagraph")
            ]

            # Combine content into plain text with newlines
            clean_text = "\n".join(content)

            return clean_text
        else:
            return ""
