from app.utils.feed_urls import feed_urls
import dateparser
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from app.utils.helper_classes.ReutersScraper import ReutersScraper
from pymongo import MongoClient, UpdateOne, errors
import feedparser
import concurrent.futures
from unidecode import unidecode


class MongoDBClient:
    def __init__(self, connection_string, db_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]

    def insert_documents(self, collection_name, document_list):
        try:
            collection = self.db[collection_name]
            operations = [
                UpdateOne({"_id": document["_id"]}, {"$set": document}, upsert=True)
                for document in document_list
            ]

            if operations:
                collection.bulk_write(operations)

        except errors.BulkWriteError as e:
            raise e

    def find_documents(self, collection_name, query, keys_to_include={}):
        collection = self.db[collection_name]
        return collection.find(query, keys_to_include).limit(10)

    def find_documents_count(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.count_documents(query)


class FeedParser:
    """A class to parse XML feed data"""

    @staticmethod
    def rss_feeds(media_origin, source_name, genre, url, feed_with_content):
        """A method to convert XML data to JSON"""
        if source_name == "Reuters" or source_name == "AP-News":
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "priority": "u=0, i",
                "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Linux"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            }
            source_name == "Reuters" and headers.update(
                {"cookie": os.environ.get("COOKIES")}
            )
            response = requests.get(url, headers=headers)
            feed = feedparser.parse(response.text)
        else:
            feed = feedparser.parse(url)
        results = []
        document_list = []
        content = ""
        tags = []
        # Max number of threads to use
        max_threads = 10 if source_name == "Reuters" else 20

        # Extract Last Build Date of Feed
        lastBuildDate = feed.get("feed").get("published")

        if not lastBuildDate:
            lastBuildDate = feed.get("feed").get("updated")

        for news_item in feed["items"]:
            if "content" in news_item:
                content = (
                    news_item.get("content")[0]["value"]
                    if news_item.get("content")
                    else ""
                )
            elif "summary" in news_item:
                content = news_item.get("summary") if news_item.get("summary") else ""

            if "tags" in news_item:
                tags = [tag.get("term") for tag in news_item.get("tags")]

            doc_params = {}
            doc_params["news_link"] = news_item.get("link")
            doc_params["article_id"] = news_item.get("id")
            doc_params["author"] = news_item.get("author")
            doc_params["title"] = news_item.get("title")
            doc_params["media_origin"] = media_origin
            doc_params["source"] = source_name
            doc_params["genre"] = genre
            doc_params["feedBuildDate"] = lastBuildDate
            doc_params["articlePubDate"] = (
                news_item.get("published")
                if news_item.get("published")
                else news_item.get("updated")
            )
            doc_params["feed_with_content"] = feed_with_content
            doc_params["tags"] = tags
            doc_params["content"] = content

            document_list.append(doc_params)

        with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:

            def news_document_wrapper(args):
                return FeedParser.prepare_news_documents(**args)

            results = list(executor.map(news_document_wrapper, document_list))

        return results

    @staticmethod
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
        timeZone = "GMT" if media_origin == "foreign" else "%z"

        # Parsing Feed build Date
        if feedBuildDate:
            parsed_build_date = FeedParser.parse_flexible_datetime(
                feedBuildDate, timeZone
            )
            document["feedBuildDate"] = (
                datetime(**parsed_build_date) if parsed_build_date else None
            )

        # Parsing Article Publish Date
        if articlePubDate:
            parsed_pubDate = FeedParser.parse_flexible_datetime(
                articlePubDate, timeZone
            )

            document["articlePubDate"] = (
                datetime(**parsed_pubDate) if parsed_pubDate else None
            )

        if feed_with_content:
            print(f"[*] Processing Article from FEED :: {title}")
            soup = BeautifulSoup(content, "html.parser")
            document["content"] = unidecode(soup.get_text(separator=" ", strip=True))

        else:
            content = ""
            print(f"[*] Processing Article from Link :: {news_link}")
            if document.get("source", None) == "Reuters":
                scraper = ReutersScraper()
                soup = scraper.load_page(news_link)
                all_p_tags = soup.find_all(
                    lambda tag: tag.has_attr("data-testid")
                    and tag["data-testid"].startswith("paragraph-")
                )
                for p_tag in all_p_tags:
                    p_tag_text = p_tag.get_text().strip()
                    if p_tag_text.startswith("Follow @"):
                        break
                    content += p_tag_text + "\n"

            else:
                handler = feed_urls[source]["scraper"](news_link)
                content = handler.extract_content()
                soup = handler.soup

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

            if news_article_tag and document.get("source", None) != "CNBC":
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

            # Try 4th Class if content still not found
            if not content:
                all_paragraphs = soup.select(".ClipPlayer-clipPlayerIntroSummary")
                if all_paragraphs:
                    content = all_paragraphs[0].text.strip()

            # Try 5th and direct method to populate content
            if not content:
                # Remove all video tags from the soup
                for video_tag in soup.find_all("video"):
                    video_tag.decompose()
                all_p_tags = soup.find_all("p")
                for p_tag in all_p_tags:
                    content += p_tag.get_text().strip() + "\n"

            document["content"] = content

        return document

    @staticmethod
    def unpack_datetime(parsed_date):
        # Extract the individual date and time components

        return {
            "year": parsed_date.year,
            "month": parsed_date.month,
            "day": parsed_date.day,
            "hour": parsed_date.hour,
            "minute": parsed_date.minute,
            "second": parsed_date.second,
        }

    @staticmethod
    def parse_flexible_datetime(str_date, timeZone=timezone.utc):
        """
        Parses a flexible datetime string, handling multiple formats and missing
        timezones. Falls back to `dateparser` for complex cases.
        """

        # Potential common datetime formats
        potential_formats = [
            "%a, %d %b %Y %H:%M:%S %z",  # e.g., "Thu, 09 Jan 2025 04:59:01 +0100"
            "%a, %d %b %Y %H:%M %z",  # e.g., "Thu, 09 Jan 2025 04:59 +0100"
            "%Y-%m-%d %H:%M:%S",  # e.g., "2025-01-09 04:59:01"
            "%Y-%m-%d %H:%M",  # e.g., "2025-01-09 04:59"
            "%d %b %Y %H:%M:%S",  # e.g., "09 Jan 2025 04:59:01"
            "%d %b %Y %H:%M",  # e.g., "09 Jan 2025 04:59"
            "%Y-%m-%dT%H:%M:%SZ",  # e.g., "2025-01-09T04:59:01Z" (ISO 8601 UTC)
        ]

        # First, try parsing with known formats
        for format_str in potential_formats:
            try:
                parsed_datetime = datetime.strptime(str_date, format_str)
                # Handle missing timezone by applying default
                if not parsed_datetime.tzinfo:
                    parsed_datetime = parsed_datetime.replace(tzinfo=timeZone)
                return FeedParser.unpack_datetime(parsed_datetime)
            except ValueError:
                pass

        # Fallback to dateparser
        try:
            parsed_datetime = dateparser.parse(
                str_date, settings={"RETURN_AS_TIMEZONE_AWARE": True}
            )
            if parsed_datetime is None:
                raise ValueError("Date parsing failed")
            # Handle missing timezone
            if parsed_datetime.tzinfo is None:
                parsed_datetime = parsed_datetime.replace(tzinfo=timeZone)
            return FeedParser.unpack_datetime(parsed_datetime)
        except Exception as e:
            print(f"Error parsing date: {e}")
            return None
