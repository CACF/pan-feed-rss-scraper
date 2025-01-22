from bs4 import BeautifulSoup
import requests


class CNBC_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self) -> str:
        all_paragraphs = self.soup.find("div", class_="ArticleBody-articleBody")
        content = ""

        if all_paragraphs:
            # Remove <div> tags with the class "PlayButton-container"
            for div_tag in all_paragraphs.find_all(
                "div", class_="PlayButton-container"
            ):
                div_tag.decompose()

            # Remove <div> tags with the id "RegularArticle-RelatedQuotes"
            for div_tag in all_paragraphs.find_all(
                "div", id="RegularArticle-RelatedQuotes"
            ):
                div_tag.decompose()

            # Remove <div> tags with the id "RegularArticle-RelatedContent-1"
            for div_tag in all_paragraphs.find_all(
                "div", id="RegularArticle-RelatedContent-1"
            ):
                div_tag.decompose()

            # Collect content from all <ul> tags, ensuring spaces between multiple tags' content
            for ul_tag in all_paragraphs.find_all("ul"):
                ul_text = " ".join(ul_tag.stripped_strings)
                content += ul_text + "\n"

            # Remove <p> tags containing <strong> tags and subsequent <ul> tags
            for p_tag in all_paragraphs.find_all("p"):
                if p_tag.find("strong"):
                    next_sibling = p_tag.find_next_sibling()
                    if next_sibling and next_sibling.name == "ul":
                        next_sibling.decompose()
                    p_tag.decompose()

            # Remove <div> tags with data-test="RelatedLinks"
            for div_tag in all_paragraphs.find_all(
                "div", {"data-test": "RelatedLinks"}
            ):
                div_tag.decompose()

            # Remove <div> tags with class InlineVideo-styles-makeit-videoFooter--e7N16
            for div_tag in all_paragraphs.find_all(
                "div", class_="InlineVideo-styles-makeit-videoFooter--e7N16"
            ):
                div_tag.decompose()

            # Remove <div> tags with class RelatedQuotes-titleAndTime undefined
            for div_tag in all_paragraphs.find_all(
                "div", class_="RelatedQuotes-titleAndTime undefined"
            ):
                div_tag.decompose()

            # Remove <div> tags with class InlineImage-imageEmbedCaption
            for div_tag in all_paragraphs.find_all(
                "div", class_="InlineImage-imageEmbedCaption"
            ):
                div_tag.decompose()

            # Remove <div> tags with id Placeholder-ArticleBody-Video-107426770
            for div_tag in all_paragraphs.find_all(
                "div", id="Placeholder-ArticleBody-Video-107426770"
            ):
                div_tag.decompose()

            for div_tag in all_paragraphs.find_all(
                "div", class_="InlineImage-imageEmbed"
            ):
                div_tag.decompose()

            for div_tag in all_paragraphs.find_all(
                "div", class_="RelatedContent-relatedContent"
            ):
                div_tag.decompose()

            # Combine the cleaned paragraph text and the ul content
            final_content = all_paragraphs.text.strip() + "\n\n" + content.strip()
            return final_content.strip()

        return ""
