from bs4 import NavigableString

class The_News_Scraper:
    def __init__(self, document, soup):
        self.document = document
        self.soup = soup
    def process(self):
        story_detail_div = self.soup.find("div", {"class": "story-detail"})
        if not story_detail_div:
            story_detail_div = self.soup.find("div", {"class": "detail-desc"})
        seen_content = set()  # Set to keep track of unique paragraph texts
        content = ""
        
        # Attempt to find all 'p' tags within this div
        p_tags = story_detail_div.find_all('p')
        if p_tags:            
            # Handle the preceding table with a single character
            first_char = ""
            preceding_table = story_detail_div.find_previous('table') if story_detail_div else None
            if preceding_table:
                table_text = preceding_table.get_text(strip=True)
                if len(table_text) == 1:
                    first_char = table_text

            if story_detail_div:
                first_p = True  # Track if it's the first paragraph
                for element in story_detail_div.find_all():
                    # Attempt to find all 'p' tags within this div
                    if element.name == 'p' or element.name == 'h1':
                        if element.find_parent('footer'):
                            continue  # Skip this <p> tag because it's inside a <footer>

                        # Remove all <b> tags within the current <p> tag
                        for b_tag in element.find_all('b'):
                            b_tag.decompose()

                        # Get the text of the <p> tag, excluding <b> tags
                        paragraph_text = element.get_text(strip=True)

                        # Merge the single character from the table with the first paragraph
                        if first_p and first_char:
                            paragraph_text = first_char + paragraph_text
                            first_char = ""  # Clear after merging
                            first_p = False  # Update flag after processing the first paragraph

                        # Check if the paragraph starts with a dash or an at symbol or if it's already seen
                        if paragraph_text.startswith('–') or paragraph_text.startswith('@') or paragraph_text in seen_content:
                            continue  # Skip adding this paragraph text to the content

                        # Add unique and valid paragraph text to the set and content
                        seen_content.add(paragraph_text)
                        content += paragraph_text + "\n\n"
                    elif element.name == 'ul':
                        list_items = element.find_all('li')
                        for li in list_items:
                            content += li.get_text(strip=True) + "\n"
                        content += "\n"  # Add extra newline after list
        if not p_tags:
            content = story_detail_div.get_text(strip=True)
        return content  # Optionally return the content, if needed elsewhere
        