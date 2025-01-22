from bs4 import BeautifulSoup
import requests


class PocketLint_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self) -> str:
        content = self.soup.find(
            "div",
            class_="content-block-regular",
        )

        if content:
            article = []
            for elem in content.find_all(["p", "h2", "h3"]):
                if elem.name == "p":
                    if elem.get("class"):
                        continue

                article.append(elem.get_text(strip=True))

            clean_text = "\n".join(article)

            return clean_text
        else:
            return ""
