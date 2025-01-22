from app.utils.helper_classes.AlJazeeraScraper import AlJazeera_Scraper
from app.utils.helper_classes.AndroidAuthorityScraper import AndroidAuthority_Scraper
from app.utils.helper_classes.AppInsiderScraper import AppInsider_Scraper
from app.utils.helper_classes.ArianaScraper import Ariana_Scraper
from app.utils.helper_classes.BBCScraper import BBC_Scraper
from app.utils.helper_classes.CNBCScraper import CNBC_Scraper
from app.utils.helper_classes.GSMArenaScraper import GSMArena_Scraper
from app.utils.helper_classes.IGNScraper import IGN_Scraper
from app.utils.helper_classes.LivemintScraper import Livemint_Scraper
from app.utils.helper_classes.NinetoFiveGoogleScraper import NinetoFiveGoogle_Scraper
from app.utils.helper_classes.PocketLintScraper import PocketLint_Scraper
from app.utils.helper_classes.TechCrunchScraper import TechCrunch_Scraper
from app.utils.helper_classes.TechRadarScraper import TechRadar_Scraper
from app.utils.helper_classes.TheGuardianScraper import The_Guardian_Scraper
from app.utils.helper_classes.TheNewsScraper import The_News_Scraper
from app.utils.helper_classes.ZDNetScraper import ZDNet_Scraper


feed_urls = {
    "AP-News": {
        "media_origin": "foreign",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://rsshub.app/apnews/topics/apf-topnews",
            },
            {
                "genre": "World-News",
                "url": "https://rsshub.app/apnews/topics/world-news",
            },
            {
                "genre": "Politics",
                "url": "https://rsshub.app/apnews/topics/politics",
            },
            {
                "genre": "US-News",
                "url": "https://rsshub.app/apnews/topics/us-news",
            },
            {
                "genre": "Sports",
                "url": "https://rsshub.app/apnews/topics/sports",
            },
            {
                "genre": "Entertainment",
                "url": "https://rsshub.app/apnews/topics/entertainment",
            },
            {
                "genre": "Entertainment",
                "url": "https://rsshub.app/apnews/topics/lifestyle",
            },
            {
                "genre": "Business",
                "url": "https://rsshub.app/apnews/topics/business",
            },
            {
                "genre": "Science-Technology",
                "url": "https://rsshub.app/apnews/topics/technology",
            },
            {
                "genre": "Science-Technology",
                "url": "https://rsshub.app/apnews/topics/science",
            },
            {
                "genre": "Health",
                "url": "https://rsshub.app/apnews/topics/health",
            },
            {
                "genre": "Environment",
                "url": "https://rsshub.app/apnews/topics/climate-and-environment",
            },
        ],
    },
    "Reuters": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://rsshub.app/reuters/breakingviews",
            },
            {
                "genre": "World-News",
                "url": "https://rsshub.app/reuters/world",
            },
            {
                "genre": "African-News",
                "url": "https://rsshub.app/reuters/world/africa",
            },
            {
                "genre": "Americas-News",
                "url": "https://rsshub.app/reuters/world/americas",
            },
            {
                "genre": "Asia-Pacific-News",
                "url": "https://rsshub.app/reuters/world/asia-pacific",
            },
            {
                "genre": "Europe-News",
                "url": "https://rsshub.app/reuters/world/europe",
            },
            {
                "genre": "Indian-News",
                "url": "https://rsshub.app/reuters/world/india",
            },
            {
                "genre": "Middle-East-News",
                "url": "https://rsshub.app/reuters/world/middle-east",
            },
            {
                "genre": "UK-News",
                "url": "https://rsshub.app/reuters/world/uk",
            },
            {
                "genre": "US-News",
                "url": "https://rsshub.app/reuters/world/us",
            },
            {
                "genre": "China-News",
                "url": "https://rsshub.app/reuters/world/china",
            },
            {
                "genre": "Entertainment",
                "url": "https://rsshub.app/reuters/business/media-telecom",
            },
            {
                "genre": "Business",
                "url": "https://rsshub.app/reuters/business/finance",
            },
            {
                "genre": "Business",
                "url": "https://rsshub.app/reuters/business/retail-consumer",
            },
            {
                "genre": "Business",
                "url": "https://rsshub.app/reuters/business/sustainable-business",
            },
            {
                "genre": "Business",
                "url": "https://rsshub.app/reuters/business/future-of-money",
            },
            {
                "genre": "Science-Technology",
                "url": "https://rsshub.app/reuters/technology",
            },
            {
                "genre": "Health",
                "url": "https://rsshub.app/reuters/business/healthcare-pharmaceuticals",
            },
            {
                "genre": "Health",
                "url": "https://rsshub.app/reuters/business/future-of-health",
            },
            {
                "genre": "Environment",
                "url": "https://rsshub.app/reuters/business/environment",
            },
            {
                "genre": "Energy",
                "url": "https://rsshub.app/reuters/business/energy",
            },
            {
                "genre": "Autos",
                "url": "https://rsshub.app/reuters/business/autos-transportation",
            },
            {
                "genre": "Autos",
                "url": "https://rsshub.app/reuters/business/charged",
            },
            {
                "genre": "Defense-Aerospace",
                "url": "https://rsshub.app/reuters/business/aerospace-defense",
            },
        ],
    },
    "CNBC": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": CNBC_Scraper,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100003114",
            },
            {
                "genre": "World-News",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100727362",
            },
            {
                "genre": "US-News",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15837362",
            },
            {
                "genre": "Asia-News",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19832390",
            },
            {
                "genre": "Europe-News",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19794221",
            },
            {
                "genre": "Politics",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000113",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001147",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839135",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=20910258",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001054",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000116",
            },
            {
                "genre": "Business",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=44877279",
            },
            {
                "genre": "Science-Technology",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910",
            },
            {
                "genre": "Travel",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000739",
            },
            {
                "genre": "Health",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000108",
            },
            {
                "genre": "Real-Estate",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000115",
            },
            {
                "genre": "Autos",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000101",
            },
            {
                "genre": "Energy",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19836768",
            },
            {
                "genre": "Entertainment",
                "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000110",
            },
        ],
    },
    "The-News": {
        "media_origin": "local",
        "feed_with_content": False,
        "scraper": The_News_Scraper,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://www.thenews.com.pk/rss/2/24",
            },
            {
                "genre": "Pakistan-News",
                "url": "https://www.thenews.com.pk/rss/1/1",
            },
            {
                "genre": "Pakistan-News",
                "url": "https://www.thenews.com.pk/rss/2/14",
            },
            {
                "genre": "Sindh-News",
                "url": "https://www.thenews.com.pk/rss/2/16",
            },
            {
                "genre": "Punjab-News",
                "url": "https://www.thenews.com.pk/rss/2/17",
            },
            {
                "genre": "KPK-News",
                "url": "https://www.thenews.com.pk/rss/2/19",
            },
            {
                "genre": "Islamabad-News",
                "url": "https://www.thenews.com.pk/rss/2/18",
            },
            {
                "genre": "World-News",
                "url": "https://www.thenews.com.pk/rss/1/2",
            },
            {
                "genre": "World-News",
                "url": "https://www.thenews.com.pk/rss/2/13",
            },
            {
                "genre": "World-News",
                "url": "https://www.thenews.com.pk/rss/2/13",
            },
            {
                "genre": "Sports",
                "url": "https://www.thenews.com.pk/rss/1/3",
            },
            {
                "genre": "Sports",
                "url": "https://www.thenews.com.pk/rss/2/22",
            },
            {
                "genre": "Business",
                "url": "https://www.thenews.com.pk/rss/1/4",
            },
            {
                "genre": "Business",
                "url": "https://www.thenews.com.pk/rss/2/15",
            },
            {
                "genre": "Business",
                "url": "https://www.thenews.com.pk/rss/1/51",
            },
            {
                "genre": "Business",
                "url": "https://www.thenews.com.pk/rss/3/28",
            },
            {
                "genre": "Politics",
                "url": "https://www.thenews.com.pk/rss/1/8",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/9",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/10",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/33",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/35",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/36",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/40",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/41",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/44",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/50",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/1/53",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.thenews.com.pk/rss/4/55",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.thenews.com.pk/rss/1/11",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.thenews.com.pk/rss/1/45",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.thenews.com.pk/rss/1/54",
            },
            {
                "genre": "Health",
                "url": "https://www.thenews.com.pk/rss/1/12",
            },
            {
                "genre": "Environment",
                "url": "https://www.thenews.com.pk/rss/1/34",
            },
            {
                "genre": "Wildlife",
                "url": "https://www.thenews.com.pk/rss/1/38",
            },
        ],
    },
    "Express-Tribune": {
        "media_origin": "local",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://tribune.com.pk/feed/latest",
            },
            {
                "genre": "Politics",
                "url": "https://tribune.com.pk/feed/politics",
            },
            {
                "genre": "Pakistan-News",
                "url": "https://tribune.com.pk/feed/pakistan",
            },
            {
                "genre": "Sindh-News",
                "url": "https://tribune.com.pk/feed/sindh",
            },
            {
                "genre": "Punjab-News",
                "url": "https://tribune.com.pk/feed/punjab",
            },
            {
                "genre": "Balochistan-News",
                "url": "https://tribune.com.pk/feed/balochistan",
            },
            {
                "genre": "KPK-News",
                "url": "https://tribune.com.pk/feed/khyber-pakhtunkhwa",
            },
            {
                "genre": "Kashmir-News",
                "url": "https://tribune.com.pk/feed/jammu-kashmir",
            },
            {
                "genre": "Gilgat-Baltistan-News",
                "url": "https://tribune.com.pk/feed/gilgit-baltistan",
            },
            {
                "genre": "World-News",
                "url": "https://tribune.com.pk/feed/world",
            },
            {
                "genre": "Sports",
                "url": "https://tribune.com.pk/feed/cricket",
            },
            {
                "genre": "Sports",
                "url": "https://tribune.com.pk/feed/sports",
            },
            {
                "genre": "Health",
                "url": "https://tribune.com.pk/feed/health",
            },
            {
                "genre": "Health",
                "url": "https://tribune.com.pk/feed/advice",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/movies",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/style",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/life-style",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/music",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/film",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/art-books",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/fashion",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/gossip",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/tv",
            },
            {
                "genre": "Entertainment",
                "url": "https://tribune.com.pk/feed/theatre",
            },
            {
                "genre": "Business",
                "url": "https://tribune.com.pk/feed/business",
            },
            {
                "genre": "Science-Technology",
                "url": "https://tribune.com.pk/feed/technology",
            },
            {
                "genre": "Science-Technology",
                "url": "https://tribune.com.pk/feed/games",
            },
            {
                "genre": "Science-Technology",
                "url": "https://tribune.com.pk/feed/gadget",
            },
        ],
    },
    "Al-Jazeera": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": AlJazeera_Scraper,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://www.aljazeera.com/xml/rss/all.xml",
            },
        ],
    },
    "BBC": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": BBC_Scraper,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://feeds.bbci.co.uk/news/rss.xml",
            },
            {
                "genre": "World-News",
                "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
            },
            {
                "genre": "UK-News",
                "url": "https://feeds.bbci.co.uk/news/uk/rss.xml",
            },
            {
                "genre": "Business",
                "url": "https://feeds.bbci.co.uk/news/business/rss.xml",
            },
            {
                "genre": "Politics",
                "url": "https://feeds.bbci.co.uk/news/politics/rss.xml",
            },
            {
                "genre": "Health",
                "url": "https://feeds.bbci.co.uk/news/health/rss.xml",
            },
            {
                "genre": "Environment",
                "url": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
            },
            {
                "genre": "Science-Technology",
                "url": "https://feeds.bbci.co.uk/news/technology/rss.xml",
            },
            {
                "genre": "Entertainment",
                "url": "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
            },
        ],
    },
    "DW-News": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://rss.dw.com/rdf/rss-en-top",
            },
            {
                "genre": "German-News",
                "url": "https://rss.dw.com/rdf/rss-en-ger",
            },
            {
                "genre": "World-News",
                "url": "https://rss.dw.com/rdf/rss-en-world",
            },
            {
                "genre": "Europe-News",
                "url": "https://rss.dw.com/rdf/rss-en-eu",
            },
            {
                "genre": "Business",
                "url": "https://rss.dw.com/rdf/rss-en-bus",
            },
            {
                "genre": "Science-Technology",
                "url": "https://rss.dw.com/xml/rss_en_science",
            },
            {
                "genre": "Environment",
                "url": "https://rss.dw.com/xml/rss_en_environment",
            },
            {
                "genre": "Entertainment",
                "url": "https://rss.dw.com/rdf/rss-en-cul",
            },
            {
                "genre": "Sports",
                "url": "https://rss.dw.com/rdf/rss-en-sports",
            },
            {
                "genre": "Asia-News",
                "url": "https://rss.dw.com/rdf/rss-en-asia",
            },
        ],
    },
    "The-Guardian": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": The_Guardian_Scraper,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://www.theguardian.com/theguardian/mainsection/topstories/rss",
            },
            {
                "genre": "African-News",
                "url": "https://www.theguardian.com/world/africa/rss",
            },
            {
                "genre": "Americas-News",
                "url": "https://www.theguardian.com/world/americas/rss",
            },
            {
                "genre": "Asia-Pacific-News",
                "url": "https://www.theguardian.com/world/asia-pacific/rss",
            },
            {
                "genre": "Australian-News",
                "url": "https://www.theguardian.com/australia-news/rss",
            },
            {
                "genre": "Europe-News",
                "url": "https://www.theguardian.com/world/europe-news/rss",
            },
            {
                "genre": "Middle-East-News",
                "url": "https://www.theguardian.com/world/middleeast/rss",
            },
            {
                "genre": "South-And-Central-Asia-News",
                "url": "https://www.theguardian.com/world/south-and-central-asia/rss",
            },
            {
                "genre": "Bangladesh-News",
                "url": "https://www.theguardian.com/world/bangladesh/rss",
            },
            {
                "genre": "Indian-News",
                "url": "https://www.theguardian.com/world/india/rss",
            },
            {
                "genre": "UK-News",
                "url": "https://www.theguardian.com/uk-news/rss",
            },
            {
                "genre": "US-News",
                "url": "https://www.theguardian.com/us-news/rss",
            },
            {
                "genre": "Ukraine-News",
                "url": "https://www.theguardian.com/world/ukraine/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/series/the-age-of-extinction/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/series/seascape-the-state-of-our-oceans/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/farming/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/climate-crisis/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/conservation/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/carbon-emissions/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/fossil-fuels/rss",
            },
            {
                "genre": "Environment",
                "url": "https://www.theguardian.com/environment/deforestation/rss",
            },
            {
                "genre": "Wildlife",
                "url": "https://www.theguardian.com/environment/wildlife/rss",
            },
            {
                "genre": "Wildlife",
                "url": "https://www.theguardian.com/world/animal-welfare/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/science/space/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/science+tone/news/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/uk/technology/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/technology/smartphones/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/technology/gadgets/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/games/rss",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.theguardian.com/science/rss",
            },
            {
                "genre": "Business",
                "url": "https://www.theguardian.com/uk/business/rss",
            },
            {
                "genre": "Health",
                "url": "https://www.theguardian.com/society/health/rss",
            },
            {
                "genre": "Health",
                "url": "https://www.theguardian.com/society/mental-health/rss",
            },
            {
                "genre": "Health",
                "url": "https://www.theguardian.com/science/medical-research/rss",
            },
            {
                "genre": "Health",
                "url": "https://www.theguardian.com/society/nhs/rss",
            },
            {
                "genre": "Health",
                "url": "https://www.theguardian.com/world/coronavirus-outbreak/rss",
            },
            {
                "genre": "Health",
                "url": "https://www.theguardian.com/lifeandstyle/health-and-wellbeing/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/football/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/cricket/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/rugby-union/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/tennis/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/cycling/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/formulaone/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/golf/rss",
            },
            {
                "genre": "Sports",
                "url": "https://www.theguardian.com/sport/us-sport/rss",
            },
            {
                "genre": "Energy",
                "url": "https://www.theguardian.com/environment/energy/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/lifeandstyle/gardens/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/books/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/music/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/uk/tv-and-radio/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/culture/marvel/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/uk/film/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/film/drama/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/fashion/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/film/horror/rss",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.theguardian.com/culture/comedy/rss",
            },
        ],
    },
    "Abb Takk TV": {
        "media_origin": "local",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://abbtakk.tv/en/feed/",
            },
        ],
    },
    "SUCH-TV": {
        "media_origin": "local",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://www.suchtv.pk/latest-news.feed",
            },
            {
                "genre": "Pakistan-News",
                "url": "https://www.suchtv.pk/pakistan.feed",
            },
            {
                "genre": "World-News",
                "url": "https://www.suchtv.pk/world.feed",
            },
            {
                "genre": "Business",
                "url": "https://www.suchtv.pk/business.feed",
            },
            {
                "genre": "Sports",
                "url": "https://www.suchtv.pk/sports.feed",
            },
            {
                "genre": "Science-Technology",
                "url": "https://www.suchtv.pk/technology.feed",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.suchtv.pk/entertainment.feed",
            },
            {
                "genre": "Health",
                "url": "https://www.suchtv.pk/health.feed",
            },
        ],
    },
    "Ariana-News": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "query": Ariana_Scraper,
        "urls": [
            {
                "genre": "Top-News",
                "url": "https://www.ariananews.af/feed/",
            },
        ],
    },
    "GSMArena": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": GSMArena_Scraper,
        "urls": [
            {
                "genre": "Latest Articles",
                "url": "https://www.gsmarena.com/rss-news-reviews.php3",
            },
        ],
    },
    "TheVerge": {
        "media_origin": "foreign",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "All Posts",
                "url": "https://www.theverge.com/rss/index.xml",
            },
        ],
    },
    "ProPakistani": {
        "media_origin": "local",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "Tech and Telecom",
                "url": "https://propakistani.pk/category/tech-and-telecom/feed/",
            },
            {
                "genre": "Business",
                "url": "https://propakistani.pk/category/business/feed/",
            },
            {
                "genre": "Sports",
                "url": "https://propakistani.pk/category/sports/feed/",
            },
            {
                "genre": "Education",
                "url": "https://propakistani.pk/category/others/education/feed/",
            },
        ],
    },
    "Business Recorder": {
        "media_origin": "local",
        "feed_with_content": True,
        "urls": [
            {
                "genre": "Latest News",
                "url": "https://www.brecorder.com/feeds/latest-news",
            },
        ],
    },
    "IGN Pakistan": {
        "media_origin": "local",
        "feed_with_content": False,
        "scraper": IGN_Scraper,
        "urls": [{"genre": "Latest News", "url": "https://pk.ign.com/feed.xml"}],
    },
    "Livemint": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": Livemint_Scraper,
        "urls": [
            {"genre": "Companies", "url": "https://www.livemint.com/rss/companies"},
            {"genre": "Opinion", "url": "https://www.livemint.com/rss/opinion"},
            {"genre": "Money", "url": "https://www.livemint.com/rss/money"},
            {"genre": "Politics", "url": "https://www.livemint.com/rss/politics"},
            {"genre": "Science", "url": "https://www.livemint.com/rss/science"},
            {"genre": "Industry", "url": "https://www.livemint.com/rss/industry"},
            {"genre": "Education", "url": "https://www.livemint.com/rss/education"},
            {"genre": "Sports", "url": "https://www.livemint.com/rss/sports"},
            {"genre": "Technology", "url": "https://www.livemint.com/rss/technology"},
            {"genre": "News", "url": "https://www.livemint.com/rss/news"},
            {"genre": "Markets", "url": "https://www.livemint.com/rss/markets"},
            {"genre": "AI", "url": "https://www.livemint.com/rss/AI"},
            {"genre": "Insurance", "url": "https://www.livemint.com/rss/insurance"},
            {"genre": "Budget", "url": "https://www.livemint.com/rss/budget"},
            {"genre": "Elections", "url": "https://www.livemint.com/rss/elections"},
        ],
    },
    "9to5Google": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": NinetoFiveGoogle_Scraper,
        "urls": [
            {"genre": "Top Stories", "url": "https://9to5google.com/feed/"},
        ],
    },
    "ZDNet": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": ZDNet_Scraper,
        "urls": [
            {"genre": "Latest News", "url": "https://www.zdnet.com/news/rss.xml"},
            {
                "genre": "AI",
                "url": "https://www.zdnet.com/topic/artificial-intelligence/rss.xml",
            },
            {"genre": "Apple", "url": "https://www.zdnet.com/topic/apple/rss.xml"},
            {"genre": "Linux", "url": "https://www.zdnet.com/topic/linux/rss.xml"},
            {
                "genre": "Microsoft",
                "url": "https://www.zdnet.com/topic/microsoft/rss.xml",
            },
            {
                "genre": "Open Source",
                "url": "https://www.zdnet.com/topic/open-source/rss.xml",
            },
            {
                "genre": "Security",
                "url": "https://www.zdnet.com/topic/security/rss.xml",
            },
        ],
    },
    "TechCrunch": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": TechCrunch_Scraper,
        "urls": [
            {"genre": "Latest", "url": "https://techcrunch.com/feed/"},
            {
                "genre": "AI",
                "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
            },
            {
                "genre": "Startups",
                "url": "https://techcrunch.com/category/startups/feed/",
            },
            {
                "genre": "Venture",
                "url": "https://techcrunch.com/category/venture/feed/",
            },
            {"genre": "Apple News", "url": "https://techcrunch.com/tag/apple/feed/"},
            {
                "genre": "Apps",
                "url": "https://techcrunch.com/category/apps/feed/",
            },
            {
                "genre": "Security",
                "url": "https://techcrunch.com/category/security/feed/",
            },
        ],
    },
    "AppInsider": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": AppInsider_Scraper,
        "urls": [
            {"genre": "Latest News", "url": "https://appleinsider.com/rss/news"},
        ],
    },
    "Pocket-Lint": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": PocketLint_Scraper,
        "urls": [
            {
                "genre": "All Articles",
                "url": "https://www.pocket-lint.com/feed/",
            },
            {
                "genre": "News",
                "url": "https://www.pocket-lint.com/feed/news/",
            },
            {
                "genre": "Devices",
                "url": "https://www.pocket-lint.com/feed/devices-segment/",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.pocket-lint.com/feed/entertainment-segment/",
            },
            {
                "genre": "AR & VR",
                "url": "https://www.pocket-lint.com/feed/ar-vr/",
            },
            {
                "genre": "Cameras",
                "url": "https://www.pocket-lint.com/feed/cameras/",
            },
            {
                "genre": "Fitness Trackers",
                "url": "https://www.pocket-lint.com/feed/fitness-trackers/",
            },
            {
                "genre": "Gadgets",
                "url": "https://www.pocket-lint.com/feed/gadgets/",
            },
            {
                "genre": "Games",
                "url": "https://www.pocket-lint.com/feed/games/",
            },
            {
                "genre": "Movies & TV",
                "url": "https://www.pocket-lint.com/feed/movies-tv/",
            },
            {
                "genre": "Smart Watches",
                "url": "https://www.pocket-lint.com/feed/smartwatches/",
            },
            {
                "genre": "Speakers",
                "url": "https://www.pocket-lint.com/feed/speakers/",
            },
            {
                "genre": "Retro tech",
                "url": "https://www.pocket-lint.com/feed/retro-tech/",
            },
            {
                "genre": "Viral tech",
                "url": "https://www.pocket-lint.com/feed/viral-tech/",
            },
        ],
    },
    "Android Authority": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "query": AndroidAuthority_Scraper,
        "urls": [
            {"genre": "News", "url": "https://www.androidauthority.com/news/feed/"},
            {
                "genre": "Features Opinions",
                "url": "https://www.androidauthority.com/features/feed/",
            },
            {
                "genre": "Reviews",
                "url": "https://www.androidauthority.com/reviews/feed/",
            },
            {
                "genre": "Best products",
                "url": "https://www.androidauthority.com/best/feed/",
            },
            {
                "genre": "Authority Insights",
                "url": "https://www.androidauthority.com/tag/authority-insights/feed/",
            },
        ],
    },
    "TechRadar": {
        "media_origin": "foreign",
        "feed_with_content": False,
        "scraper": TechRadar_Scraper,
        "urls": [
            {"genre": "All Articles", "url": "https://www.techradar.com/feeds.xml"},
            {
                "genre": "News",
                "url": "https://www.techradar.com/feeds/articletype/news",
            },
            {
                "genre": "Reviews",
                "url": "https://www.techradar.com/feeds/articletype/review",
            },
            {
                "genre": "Buying Guides",
                "url": "https://www.techradar.com/feeds/articletype/best",
            },
            {
                "genre": "Deals",
                "url": "https://www.techradar.com/feeds/articletype/deals",
            },
            {
                "genre": "Features",
                "url": "https://www.techradar.com/feeds/articletype/feature",
            },
            {
                "genre": "Opinions",
                "url": "https://www.techradar.com/feeds/articletype/opinion",
            },
            {
                "genre": "Phones",
                "url": "https://www.techradar.com/feeds/tag/phones",
            },
            {
                "genre": "Televisions",
                "url": "https://www.techradar.com/feeds/tag/televisions",
            },
            {
                "genre": "Entertainment",
                "url": "https://www.techradar.com/feeds/tag/entertainment",
            },
            {
                "genre": "Health &amp; fitness",
                "url": "https://www.techradar.com/feeds/tag/health-fitness",
            },
            {
                "genre": "Computing",
                "url": "https://www.techradar.com/feeds/tag/computing",
            },
            {
                "genre": "Computing components",
                "url": "https://www.techradar.com/feeds/tag/computing-components",
            },
            {
                "genre": "Smart home",
                "url": "https://www.techradar.com/feeds/tag/smart-home",
            },
            {
                "genre": "Gaming",
                "url": "https://www.techradar.com/feeds/tag/gaming",
            },
            {
                "genre": "Audio",
                "url": "https://www.techradar.com/feeds/tag/audio",
            },
            {
                "genre": "Home cinema",
                "url": "https://www.techradar.com/feeds/tag/home-cinema",
            },
            {
                "genre": "Internet",
                "url": "https://www.techradar.com/feeds/tag/internet",
            },
            {
                "genre": "Cameras",
                "url": "https://www.techradar.com/feeds/tag/cameras",
            },
            {
                "genre": "Software",
                "url": "https://www.techradar.com/feeds/tag/software",
            },
            {
                "genre": "Home",
                "url": "https://www.techradar.com/feeds/tag/home",
            },
        ],
    },
}
