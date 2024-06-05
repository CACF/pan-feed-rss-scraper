from bs4 import BeautifulSoup
from unidecode import unidecode
import requests
def prepare_news_documents(
        news_link,
        media_origin,
        title,
        source,
        genre,
        feedBuildDate,
        article_id,
        articlePubDate,
        feed_with_content,
        content,
        tags=[],
        author="",
        language="en-us",
    ):
        """Method to prepare the single news document for mongoDB"""

        document = {}
        news_link = "https://www.aljazeera.com/news/2023/12/15/russia-ukraine-war-list-of-key-events-day-660"
        document["_id"] = news_link
        document["media_origin"] = media_origin
        document["source"] = source
        document["genre"] = genre
        document["language"] = language
        document["article_id"] = article_id
        document["authors"] = author if author else source
        document["title"] = title
        document["tags"] = tags

        # check the time zones for foreign & local media
        
        # Parsing Feed build Date
        # if feedBuildDate:
        #     parsed_build_date = FeedParser.parse_flexible_datetime(
        #         feedBuildDate, timeZone
        #     )
        #     document["feedBuildDate"] = (
        #         datetime(*parsed_build_date) if parsed_build_date else None
        #     )

        # # Parsing Article Publish Date
        # if articlePubDate:
        #     parsed_pubDate = FeedParser.parse_flexible_datetime(
        #         articlePubDate, timeZone
        #     )
        #     document["articlePubDate"] = (
        #         datetime(*parsed_pubDate) if parsed_pubDate else None
        #     )

        if feed_with_content:
            print(f"[*] Processing Article from FEED :: {title}")
            soup = BeautifulSoup(content, "html.parser")
            # soup = BeautifulSoup(unescape(content), "lxml")
            document["content"] = unidecode(soup.get_text(separator=" ", strip=True))

        else:
            content = ""
            print(f"[*] Processing Article from Link :: {news_link}")
            if document.get('source', None) == 'Reuters':
                pass
                # scraper = ReutersScraper()
                # soup = scraper.load_page(news_link)
                # all_p_tags = soup.find_all(lambda tag: tag.has_attr('data-testid') and tag['data-testid'].startswith('paragraph-'))
                # for p_tag in all_p_tags:
                #     p_tag_text = p_tag.get_text().strip()
                #     if p_tag_text.startswith("Follow @"):
                #         break
                #     content += p_tag_text + "\n"
                # scraper.close()
                
            else:
                # # Request and Grab html
                res = requests.get(news_link)
                soup = BeautifulSoup(res.text, "html.parser")

                # if document.get('source', None) == 'The-News':
                #     handler = The_News_Scraper(document, soup)
                #     content = handler.process()

                # elif document.get('source', None) == 'The-Guardian':
                #     handler = The_Guardian_Scraper(soup)
                #     content = handler.extract_content()

                # elif document.get('source', None) == 'BBC':
                #     handler = BBC_Scraper(soup)
                #     content = handler.extract_content()

                # elif document.get('source', None) == 'CNBC':
                #     handler = CNBC_Scraper(soup)
                #     content = handler.extract_content()

            # Extracting document Title if not present in feed
            if not title:
                title = soup.find("h1")
                document["title"] = title.text.strip() if title else ""

            # Parsing Tags for news document
            tags = (
                soup.find("meta", {"name": "keywords"})["content"].split(",")
                if soup.find("meta", {"name": "keywords"})
                else []
            )
            document["tags"] = list(set(tags))

            # Try 1st Class
            news_article_tag = soup.select(".ArticleBody-articleBody")

            # Try 2nd Class if content not found
            if not news_article_tag:
                news_article_tag = soup.select(".FeaturedContent-articleBody")

            if news_article_tag:
                all_paragraphs = news_article_tag[0].find_all("p")
                parsed_paragraphs = [
                    single_para.text.strip() for single_para in all_paragraphs
                ]
                content = content.join(parsed_paragraphs)

            # Try 3rd Class if content still not found
            if not content:
                all_paragraphs = soup.find("div", {"data-module": "ArticleBody"})
                if all_paragraphs:
                    content = all_paragraphs.text.strip()
                print("First", content)

            # Try 4th Class if content still not found
            if not content:
                all_paragraphs = soup.select(".ClipPlayer-clipPlayerIntroSummary")
                if all_paragraphs:
                    content = all_paragraphs[0].text.strip()
                print("Second", content)

            # Try 5th and direct method to populate content
            if not content:
                all_p_tags = soup.find_all("p")
                for p_tag in all_p_tags:
                    content += p_tag.get_text().strip() + "\n"
                print("Third", content)

            document["content"] = content

        print(document)


prepare_news_documents(news_link='https://www.aljazeera.com/news/2024/6/4/uks-sunak-and-starmer-to-clash-in-debate-as-farage-enters-election-fray?traffic_source=rss',
        media_origin='foreign',
        title='French military trainers would be ‘legitimate target’ in Ukraine: Lavrov',
        source='Al-Jazeera',
        genre='Top-News',
        feedBuildDate='Wed, 05 Jun 2024 04:47:45 +0000',
        article_id='https://www.aljazeera.com/?t=1717547744',
        articlePubDate='Tue, 04 Jun 2024 15:41:56 +0000',
        feed_with_content=False,
        content='Indian Prime Minister Narendra Modi appears set to retain power at the head of a governing coalition.',
        tags=['News'],
        author="Fawad Azher",
        language="en-us",
    )