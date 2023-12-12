# Simple PAN-FEED-RSS With Fastapi (Python 3)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have installed Python 3 on your device

### Project structure
```
* pan-feed-rss-scraper/
  |--- app/
  |    |--- utils
  |    |    |--- feed_urls.py
  |    |    |--- feed_utilities.py
  |    |--- v1
  |    |    |--- blueprints.py
  |    |    |--- feed_blc.py
  |--- .env
  |--- .gitignore
  |--- Dockerfile
  |--- README.md  
  |--- requirements.txt
  |--- run.py
```


A step by step series of examples that tell you how to get a development env running

1. Install virtual environment
```
pip install virtualenv
```
2. Create virtual environment and activate inside your admin-api directory according the above structure
```
virtualenv venv
> On windows -> venv\Scripts\activate
> On linux -> source venv/bin/activate
```
3. Change directory into admin-api folder.
```
cd pan-feed-rss-scraper
```
4. Install some librares on your virtual environment with pip
```
pip install -r requirements.txt
```
5. Create .env file if not exists and set environment variables for database. i.e.
```
MONGO_HOST=127.0.0.1
MONGO_PORT="27017"
DATABASE="pan"
COLLECTION="news"
HOST=0.0.0.0
PORT=1010
ENVIRONMENT=development
```
5. Run the local server with this command
```
py run.py --reload
```

## Clone or Download

You can clone or download this project
```
> Clone : https://github.com/CACF/pan-feed-rss-scraper.git
```

## Authors

* **Fawad Azher** - *