class CNBC_Scraper:
    def __init__(self, soup):
        self.soup = soup

    def extract_content(self) -> str:
        all_paragraphs = self.soup.find("div", class_="ArticleBody-articleBody")
        if all_paragraphs:
            # Remove <p> tags containing <strong> tags and subsequent <ul> tags
            for p_tag in all_paragraphs.find_all("p"):
                if p_tag.find("strong"):
                    next_sibling = p_tag.find_next_sibling()
                    if next_sibling and next_sibling.name == "ul":
                        next_sibling.decompose()
                    p_tag.decompose()
            # Remove <div> tags with data-test="RelatedLinks"
            for div_tag in all_paragraphs.find_all("div", {"data-test": "RelatedLinks"}):
                div_tag.decompose()

            # Remove <div> tags with class InlineVideo-styles-makeit-videoFooter--e7N16
            for div_tag in all_paragraphs.find_all("div", class_="InlineVideo-styles-makeit-videoFooter--e7N16"):
                div_tag.decompose()
            # Remove <div> tags with class RelatedQuotes-titleAndTime undefined
            for div_tag in all_paragraphs.find_all("div", class_="RelatedQuotes-titleAndTime undefined"):
                div_tag.decompose()
            # Remove <div> tags with class InlineImage-imageEmbedCaption
            for div_tag in all_paragraphs.find_all("div", class_="InlineImage-imageEmbedCaption"):
                div_tag.decompose()
            # Remove <div> tags with id Placeholder-ArticleBody-Video-107426770
            for div_tag in all_paragraphs.find_all("div", id="Placeholder-ArticleBody-Video-107426770"):
                div_tag.decompose()
            for div_tag in all_paragraphs.find_all("div", class_="InlineImage-imageEmbed"):
                div_tag.decompose()
            for div_tag in all_paragraphs.find_all("div", class_="RelatedContent-relatedContent"):
                div_tag.decompose()
            return all_paragraphs.text.strip()
        return ""