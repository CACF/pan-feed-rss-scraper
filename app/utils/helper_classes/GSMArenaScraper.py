import random
from time import sleep
from bs4 import BeautifulSoup
import requests


class GSMArena_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

        # Adding slight delay in repitive requests due to GSMArena server security
        sleep(random.uniform(4, 8))

    def extract_content(self) -> str:
        content = self.soup.find("div", id="review-body")

        if content:
            paragraphs = [
                p.get_text(strip=True)
                for p in content.find_all("p")
                if "article-source" not in p.get("class", [])
            ]

            # Combine the paragraphs into a single string
            content = "\n".join(paragraphs)

            return content.replace("\\n", "\n")
        else:
            return ""
