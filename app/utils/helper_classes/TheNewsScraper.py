class The_News_Scraper:
    def __init__(self, document, soup):
        self.document = document
        self.soup = soup
    def process(self):
        all_paragraphs = self.soup.find("div", {"class": "story-detail"})
        seen_content = set()  # Set to keep track of unique paragraph texts
        content = ""
        
        if hasattr(all_paragraphs, 'find_previous'):
            # Handle the preceding h2
            preceding_h2 = all_paragraphs.find_previous('h2') if all_paragraphs else None
            if preceding_h2:
                preceding_h2_content = preceding_h2.get_text(strip=True)
                content += preceding_h2_content + ". "
                seen_content.add(preceding_h2_content)
        
        # Handle the preceding table with a single character
        first_char = ""
        preceding_table = all_paragraphs.find_previous('table') if all_paragraphs else None
        if preceding_table:
            table_text = preceding_table.get_text(strip=True)
            if len(table_text) == 1:
                first_char = table_text

        if all_paragraphs:
            first_p = True  # Track if it's the first paragraph
            for element in all_paragraphs.children:
                if element.name == 'p':
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

        return content  # Optionally return the content, if needed elsewhere
        