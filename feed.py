import os
from time import time

from feed_urls import feed_urls
from feed_utilities import FeedParser
from feed_utilities import MongoDBClient



def feed_starter():
    # document_list = list()
    total_time = 0
    print("Feed Ingestion has started !!!!\n\n")
    # URL to fetch XML data
    for feed in feed_urls:
        source_start_time = time()
        media_origin = feed.get("media_origin", "Unknown")
        source = feed.get("source", "Unknown")
        feed_with_content = feed.get("feed_with_content", False)

        if "urls" in feed:
            for url_dict in feed["urls"]:
                genre_start_time = time()
                url = url_dict.get("url")
                genre = url_dict.get("genre")

                data_list = FeedParser.rss_feeds(
                    media_origin, source, genre, url, feed_with_content
                )

                # creating an instance of MongoDB
                mongo_client = MongoDBClient("mongodb://{}:{}/".format(os.environ.get("MONGO_HOST"),os.environ.get("MONGO_PORT")), os.environ.get("DATABASE"))

                # Inserting documents into MongoDB collection
                _ = mongo_client.insert_documents(os.environ.get("COLLECTION"), data_list)

                genre_stop_time = time()
                genre_time = genre_stop_time - genre_start_time

                print(
                    "\n\n------------------------------------------------------------------------------"
                )
                print(
                    f'Feed of "{source}", "{genre.upper()}" completed in {round(genre_time, 2)} seconds'
                )
                print(
                    "------------------------------------------------------------------------------\n\n"
                )

            source_stop_time = time()
            source_time = source_stop_time - source_start_time
            total_time += source_time

            print(
                "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            )
            print(
                f'Ingestion of "{source}" all genres completed in {round(source_time, 2)} seconds'
            )
            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
            )

        else:
            print("Failed to fetch XML data. Please check the Feed Links/URLs")

    print("\n\n######################################################################")
    print(f"Ingestion of all Media-Feed completed in {round(total_time, 2)} seconds")
    print("######################################################################\n\n")

    return True
