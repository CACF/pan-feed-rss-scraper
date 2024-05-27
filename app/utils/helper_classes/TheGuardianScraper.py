from bs4 import BeautifulSoup, NavigableString

class The_Guardian_Scraper:
    def __init__(self, soup):
        self.soup = soup

    def get_filtered_text(self, element):
        text_content = ''
        for child in element.descendants:
            if isinstance(child, NavigableString):
                # Check parents for undesired tags and class 'dcr-13gln72'
                undesired_found = any(
                    parent.name in ['em', 'figure', 'img', 'header', 'footer', 'nav', 'label', 'a', 'time'] or 
                    'dcr-13gln72' in parent.get('class', [])
                    for parent in child.parents
                )
                if not undesired_found:
                    text_content += child.strip() + ' '
        return text_content
    
    def extract_content(self):
        target_div = self.soup.find('div', {'id': 'maincontent'})
        if not target_div:
            target_div = self.soup.find('div', class_='mobile-drawer')
        if not target_div.contents:
            target_div = self.soup.find('div', class_='podcast__body')
        if not target_div:
            target_div = self.soup.find('div', class_='l-side-margins')
        return self.get_filtered_text(target_div) if target_div else ""

