from bs4 import BeautifulSoup, NavigableString

class The_Guardian_Scraper:
    def __init__(self, soup):
        self.soup = soup

    def extract_content(self):
        target_div = self.soup.find('div', {'id': 'maincontent'})
        return self.get_filtered_text(target_div) if target_div else ""

    def get_filtered_text(self, element):
        text_content = ''
        for child in element.descendants:
            if isinstance(child, NavigableString):
                # Check parents for undesired tags
                undesired_found = any(parent.name in ['em', 'figure', 'img', 'header', 'footer', 'nav', 'label'] for parent in child.parents)
                if not undesired_found:
                    text_content += child.strip() + ' '
        return text_content
