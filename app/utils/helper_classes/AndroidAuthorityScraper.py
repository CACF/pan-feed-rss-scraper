from bs4 import BeautifulSoup
import requests


class AndroidAuthority_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self) -> str:
        content = self.soup.find(
            "div",
            class_="e_Ac",
        )

        if content:
            content = [
                elem.get_text(strip=True)
                for elem in content.select(
                    "div.e_e > p, div.e_e ul > li, div.e_e > h2, div.e_e > q"
                )
            ]

            clean_text = "\n".join(content)

            return clean_text
        else:
            return ""
