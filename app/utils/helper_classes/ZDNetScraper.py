from bs4 import BeautifulSoup
import requests


class ZDNet_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self) -> str:
        content = self.soup.find(
            "div",
            {"class": "c-ShortcodeContent"},
        )

        if content:
            content = [
                elem.get_text(strip=True) for elem in content.find_all(["p", "h2"])
            ]

            # Combine content into plain text with newlines
            clean_text = "\n".join(content)

            return clean_text
        else:
            return ""
