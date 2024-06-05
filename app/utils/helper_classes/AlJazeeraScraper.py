class AlJazeera_Scraper:
    def __init__(self, soup):
        self.soup = soup
        self.content = ""

    def extract_content(self):
        main_content = self.soup.find(id="main-content-area")
        if main_content:
            # Find all p and li tags, excluding those inside the specified divs and figures
            for tag in main_content.find_all(['p', 'li']):
                # Check if the tag is inside a div or figure we want to exclude
                parent_divs = tag.find_parents(["div", "figure"])
                if any(
                    "article-featured-image" in div.get("class", [])
                    or "container--ads in-article-ads" in div.get("class", [])
                    or "more-on" in div.get("class", [])
                    or div.get("class") == ["video-player-facade-container"]
                    or div.get("id") == "article-newsletter-slot"
                    for div in parent_divs
                ):
                    continue
                self.content += tag.get_text().strip() + "\n"
        return self.content