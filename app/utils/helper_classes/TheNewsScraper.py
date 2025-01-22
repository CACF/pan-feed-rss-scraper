from bs4 import BeautifulSoup
import requests


class The_News_Scraper:
    def __init__(self, link):
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def extract_content(self):
        article_content_div = self.soup.find("div", {"class": "story-detail"})
        if not article_content_div:
            article_content_div = self.soup.find("div", {"class": "detail-desc"})
        if not article_content_div:
            article_content_div = self.soup.find("div", {"class": "detail-content"})

        seen_content = set()  # Set to keep track of unique paragraph texts
        content = ""

        # Handle the preceding table with a single character
        first_char = ""
        preceding_table = (
            article_content_div.find_previous("table") if article_content_div else None
        )
        if preceding_table:
            table_text = preceding_table.get_text(strip=True)
            if len(table_text) == 1:
                first_char = table_text

        first_p = True  # Track if it's the first paragraph
        single_char_p = ""  # Track single character <p> tags

        for element in article_content_div.find_all():
            if element.name == "p" or element.name == "h1":
                if element.find_parent("footer"):
                    continue  # Skip this tag because it's inside a <footer>

                # Check if this <p> tag contains a single character
                element_text = element.get_text(strip=True)
                if len(element_text) == 1:
                    single_char_p = element_text
                    continue  # Move to the next element to merge the single character with its text

                # Remove all <b> tags within the current <p> tag
                for b_tag in element.find_all("b"):
                    b_tag.decompose()

                # Get the text of the <p> tag, excluding <b> tags
                paragraph_text = element.get_text(strip=True)

                # Merge the single character from the previous <p> with this paragraph
                if single_char_p:
                    paragraph_text = single_char_p + paragraph_text
                    single_char_p = ""  # Clear after merging

                # Merge the single character from the table with the first paragraph
                if first_p and first_char:
                    paragraph_text = first_char + paragraph_text
                    first_char = ""  # Clear after merging
                    first_p = False  # Update flag after processing the first paragraph

                # Check if the paragraph starts with a dash or an at symbol or if it's already seen
                if (
                    paragraph_text.startswith("–")
                    or paragraph_text.startswith("@")
                    or paragraph_text in seen_content
                ):
                    continue  # Skip adding this paragraph text to the content

                # Add unique and valid paragraph text to the set and content
                seen_content.add(paragraph_text)
                content += paragraph_text + "\n\n"
            elif element.name == "ul":
                list_items = element.find_all("li")
                for li in list_items:
                    content += li.get_text(strip=True) + "\n"
                content += "\n"  # Add extra newline after list

        return content  # Optionally return the content, if needed elsewhere
