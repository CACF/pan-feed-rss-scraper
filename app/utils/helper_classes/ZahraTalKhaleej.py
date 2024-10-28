class ZahraTalKhaleej_Scraper:
    def __init__(self, soup):
        self.soup = soup

    def extract_content(self):
        content = ""
        
        # Remove all video tags
        for video_tag in self.soup.find_all("video"):
            video_tag.decompose()
        
        # Remove div with class "slide-up-menu"
        for slide_up_menu in self.soup.find_all("div", class_="slide-up-menu"):
            slide_up_menu.decompose()
        
        # Remove p and h3 tags with class "hastag-title"
        for tag in self.soup.find_all(["p", "h3"], class_="hastag-title"):
            tag.decompose()
        
        # Remove ul with class "content-media-wrapper"
        for media_wrapper in self.soup.find_all("ul", class_="content-media-wrapper"):
            media_wrapper.decompose()

        # Find all remaining p tags and extract text
        all_p_tags = self.soup.find_all("p")
        for p_tag in all_p_tags:
            content += p_tag.get_text().strip() + "\n"

        return content
    