class ZahraTalKhaleej_Scraper:
    def __init__(self, soup):
        self.soup = soup

    def extract_content(self):
        content = ""
        
        # Remove all video and iframe tags
        for video_tag in self.soup.find_all("video"):
            video_tag.decompose()
        for iframe_tag in self.soup.find_all("iframe"):
            iframe_tag.decompose()
        
        # Remove div with class "slide-up-menu"
        for slide_up_menu in self.soup.find_all("div", class_="slide-up-menu"):
            slide_up_menu.decompose()
        
        # Remove p and h3 tags with class "hastag-title"
        for tag in self.soup.find_all(["p", "h3"], class_="hastag-title"):
            tag.decompose()
        
        # Remove ul with class "content-media-wrapper"
        for media_wrapper in self.soup.find_all("ul", class_="content-media-wrapper"):
            media_wrapper.decompose()

        # Find all remaining p tags and extract text, ignoring strong tags inside p
        all_p_tags = self.soup.find_all("p")
        
        for p_tag in all_p_tags:
            # Stop adding content if a div with class 'article-tags' is encountered
            if p_tag.find_previous("div", class_="article-tags"):
                break
            
            # Skip content inside a div with class 'hidden'
            if p_tag.find_parent("div", class_="hidden"):
                continue

            # Decompose all strong tags within each p tag to ignore their content
            for strong_tag in p_tag.find_all("strong"):
                strong_tag.decompose()
                
            content += p_tag.get_text().strip() + "\n"

        # Trim whitespace from the final content string
        return content.strip()
    